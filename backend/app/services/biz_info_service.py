from app.schemas.biz_info import BizInfoDataRequests, BizInfoResponse
from app.database.models import BizInfo
from openai import OpenAI
from app.common.consts import BUCKET_NAME, REGION_NAME
from app.common.config import s3_client
from app.common.utils import create_uuid
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.common.config import get_parameter

async def search_all_bizinfo_data_from_DB(db: AsyncSession):
    # 모든 BizInfo 레코드를 조회
    bizinfo_query = await db.execute(select(BizInfo))
    bizinfo_list = bizinfo_query.scalars().all()
    
    # 만약 DB에 데이터가 없는 경우 404 처리
    if not bizinfo_list:
        raise HTTPException(status_code=404, detail="No Biz info found")
    
    # category_id가 None인 경우 999로 설정하는 로직을 각 레코드에 적용
    # 또한, BizInfoResponse 모델에 맞추어 리스트 변환
    response_list = []
    for bizinfo in bizinfo_list:
        if not bizinfo.category_id:
            bizinfo.category_id = 999
        
        response_list.append(BizInfoResponse(
            biz_key = bizinfo.biz_key,
            biz_name = bizinfo.biz_name,
            biz_mail = bizinfo.biz_mail,
            biz_address = bizinfo.biz_address,
            biz_phone = bizinfo.biz_phone,
            biz_manager = bizinfo.biz_manager,
            category_id = bizinfo.category_id,
            products_categories=bizinfo.products_categories,
            price=bizinfo.price,
            main_platform=bizinfo.main_platform,
            event_type=bizinfo.event_type,
            charactor_type=bizinfo.charactor_type,
        ))
    
    return response_list

async def generate_ad_outline(bizinfo_data: BizInfoDataRequests, client):
    prompt = f"""
    다음은 광고 요청 정보다:
    1. 광고 제품: {bizinfo_data.products_categories}
    2. 예상 비용: {bizinfo_data.price}
    3. 광고 플랫폼: {bizinfo_data.main_platform}
    4. 광고 방법: {bizinfo_data.event_type}
    5. 홍보 캐릭터 성별: {bizinfo_data.charactor_type}

    위 정보를 바탕으로 광고 OUTLINE을 작성해줘.
    형식: 머릿말 - 본론(최대 3개 소제목 가능) - 맺음말
    글의 길이는 500~600자로 제한.
    """
    try:
        # 30초 타임아웃으로 OpenAI API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "너는 전문 광고 기획자다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=700,
        )
        outline = response.choices[0].message.content
        return outline
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"광고 OUTLINE 생성 중 오류가 발생했습니다: {str(e)}"
        )
    


async def insert_bizinfo_data_to_DB(bizinfo_data: BizInfoDataRequests, db: AsyncSession):
    try:
        outline = None  # outline 변수 초기화
        # OpenAI API 키 설정
        client = OpenAI(
            api_key=get_parameter("/TEST/CICD/STREAMLIT/OPENAI_API_KEY"),  # This is the default and can be omitted
        )
        # 광고 OUTLINE 생성
        try:
            # OpenAI API 키 확인
            if not client:
                raise HTTPException(
                    status_code=500, detail="OpenAI API 키가 설정되지 않았습니다."
                )
            # 광고 OUTLINE 생성
            outline = await generate_ad_outline(bizinfo_data, client)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"서버 내부 오류 발생: {str(e)}"
            )
            
        uuid = create_uuid()
        
        # 데이터베이스에 저장할 기업 정보 객체 생성
        new_bizinfo = BizInfo(
            biz_name=bizinfo_data.biz_name,
            biz_mail=bizinfo_data.biz_mail,
            biz_address=bizinfo_data.biz_address,
            biz_phone=bizinfo_data.biz_phone,
            biz_manager=bizinfo_data.biz_manager,
            category_id=bizinfo_data.category_id,
            products_categories=bizinfo_data.products_categories,
            price=bizinfo_data.price,
            main_platform=bizinfo_data.main_platform,
            event_type=bizinfo_data.event_type,
            charactor_type=bizinfo_data.charactor_type,
            outline=outline,  # 생성된 광고 OUTLINE 저장
            UUID=uuid
        )

        # 데이터 저장 및 커밋
        db.add(new_bizinfo)
        await db.commit()
        await db.refresh(new_bizinfo)

        # 성공 응답
        return {
            "Message": "기업 정보와 광고 OUTLINE이 성공적으로 저장되었습니다.",
            "biz_name": bizinfo_data.biz_name,
            "ad_outline": outline,  # 생성된 OUTLINE 포함
            "User-ID" : uuid
        }
    except Exception as e:
        # 오류 발생 시 롤백
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"데이터 저장 중 오류가 발생했습니다: {str(e)}"
        )

async def search_bizinfo_data_from_DB(biz_key:int, db: AsyncSession):
    bizinfo_query = await db.execute(select(BizInfo).where(BizInfo.biz_key == biz_key))
    bizinfo = bizinfo_query.scalar_one_or_none()
    
    if not bizinfo:
        raise HTTPException(status_code=404, detail="Biz info not found")
    
    if not bizinfo.category_id:
        bizinfo.category_id = 999
    
    return BizInfoResponse(
        biz_key = bizinfo.biz_key,
        biz_name = bizinfo.biz_name,
        biz_mail = bizinfo.biz_mail,
        biz_address = bizinfo.biz_address,
        biz_phone = bizinfo.biz_phone,
        biz_manager = bizinfo.biz_manager,
        category_id = bizinfo.category_id,
        products_categories=bizinfo.products_categories,
        price=bizinfo.price,
        main_platform=bizinfo.main_platform,
        event_type=bizinfo.event_type,
        charactor_type=bizinfo.charactor_type,
    )

async def delete_bizinfo_data_from_DB(biz_key:int, db: AsyncSession):
    bizinfo_query = await db.execute(select(BizInfo).where(BizInfo.biz_key == biz_key))
    bizinfo = bizinfo_query.scalar_one_or_none()
    
    if not bizinfo:
        raise HTTPException(status_code=404, detail="Biz info not found")
    try:
        db.delete(bizinfo)
        await db.commit()
        return {"Message": "Bizinfo Deletion Complete"}
    except:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Can't commit Biz info to DB")