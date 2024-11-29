from app.schemas.biz_contacts import BizContactsDataRequests, BizContactsDataResponce
from app.database.models import BizInfo, BizContacts
from typing import Optional
from app.common.consts import BUCKET_NAME, REGION_NAME
from app.common.config import s3_client
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.common.utils import is_valid_file_type, make_pwd_to_hash

async def insert_bizcontacts_data_to_DB(bizinfo_data: BizContactsDataRequests, db: AsyncSession):  # 서비스 로직 호출
    new_bizinfo = BizContacts(
        biz_key = bizinfo_data.biz_key,
        service_name = bizinfo_data.service_name,
        service_info = bizinfo_data.service_info,
        budget = bizinfo_data.budget,
        period = bizinfo_data.period,
        platform = bizinfo_data.platform,
        promo_info = bizinfo_data.promo_info,
        service_target = bizinfo_data.service_target,
        service_charactors = bizinfo_data.service_charactors,
        category_id = bizinfo_data.category_id
    )
    
    try:
        db.add(new_bizinfo)
        await db.commit()
        await db.refresh(new_bizinfo)
    except:
        await db.rollback()
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail = "Failed to save data"
                            )
    # Pydantic 모델로 변환하여 반환
    return {
        "message": "Success to save of biz contacts information to DB",
        "order_date":new_bizinfo.order_date,
        "service_name":new_bizinfo.service_name,
        "service_info":new_bizinfo.service_info,
        "budget":new_bizinfo.budget,
        "period":new_bizinfo.period,
        "platform":new_bizinfo.platform,
        "promo_info":new_bizinfo.promo_info,
        "service_target":new_bizinfo.service_target,
        "service_charactors":new_bizinfo.service_charactors,
    }
    
async def search_bizcontacts_data_from_DB(order_id:int, db: AsyncSession):
    bizcontacts_query = await db.execute(select(BizContacts).where(BizContacts.order_id == order_id))
    bizcontacts = bizcontacts_query.scalar_one_or_none()
    
    if not bizcontacts:
        raise HTTPException(status_code=404, detail="Biz info not found")
    
    # Pydantic 모델로 변환하여 반환
    return BizContactsDataResponce(
        order_id=bizcontacts.order_id,
        biz_key=bizcontacts.biz_key,
        order_date=bizcontacts.order_date,
        service_name=bizcontacts.service_name,
        service_info=bizcontacts.service_info,
        budget=bizcontacts.budget,
        period=bizcontacts.period,
        platform=bizcontacts.platform,
        promo_info=bizcontacts.promo_info,
        service_target=bizcontacts.service_target,
        service_charactors=bizcontacts.service_charactors,
        category_id=bizcontacts.category_id,
    )

async def delete_bizcontacts_data_from_DB(order_id:int, db: AsyncSession):
    bizinfo_query = await db.execute(select(BizContacts).where(BizContacts.order_id == order_id))
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