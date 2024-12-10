from app.schemas.biz_info import BizInfoDataRequests, BizInfoResponse
from app.database.models import BizInfo
from typing import Optional
from app.common.consts import BUCKET_NAME, REGION_NAME
from app.common.config import s3_client
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.common.utils import is_valid_file_type, make_pwd_to_hash

async def insert_bizinfo_data_to_DB(bizinfo_data: BizInfoDataRequests, db: AsyncSession):  # 서비스 로직 호출
    new_bizinfo = BizInfo(
        biz_name = bizinfo_data.biz_name,
        biz_mail = bizinfo_data.biz_mail,
        biz_address = bizinfo_data.biz_address,
        biz_phone = bizinfo_data.biz_phone,
        biz_manager = bizinfo_data.biz_manager,
        category_id = bizinfo_data.category_id,
        Q1 = bizinfo_data.Q1,
        Q2 = bizinfo_data.Q2,
        Q3 = bizinfo_data.Q3,
        Q4 = bizinfo_data.Q4,
        Q5 = bizinfo_data.Q5
    )
    try:
        db.add(new_bizinfo)
        await db.commit()
        await db.refresh(new_bizinfo)
    except:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="데이터 저장 중 오류가 발생했습니다.",
        )
    return {
        "Message": "기업 정보가 성공적으로 저장되었습니다.",
        "biz_name": bizinfo_data.biz_name,
    }
    

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
        Q1 = bizinfo.Q1,
        Q2 = bizinfo.Q2,
        Q3 = bizinfo.Q3,
        Q4 = bizinfo.Q4,
        Q5 = bizinfo.Q5
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