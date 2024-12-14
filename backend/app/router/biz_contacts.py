from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.biz_contacts import BizContactsDataRequests, BizContactsDataResponse, BizContactsUpdateModel
from app.services.biz_contacts_service import insert_bizcontacts_data_to_DB, search_bizcontacts_data_from_DB, delete_bizcontacts_data_from_DB, search_bizcontacts_data_from_DB_as_uuid, delete_bizcontacts_data_from_DB_as_uuid, update_bizcontacts_data, update_bizcontacts_data_as_uuid
from app.database.database import get_db
from app.auth.token import get_current_user  # 인증 함수
import json

router = APIRouter(prefix="/bizcontacts", tags=["Business Contact Infomation"])

# 기업 정보 저장 API
@router.post("/insert", summary="기업 광고 정보 저장", status_code=status.HTTP_201_CREATED)
async def insert_bizcontacts(bizinfo_data: BizContactsDataRequests, db: AsyncSession = Depends(get_db)):#, current_user: dict = Depends(get_current_user)):
    try:
        result = await insert_bizcontacts_data_to_DB(bizinfo_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# uuid 수정
@router.put("/{uuid}")
async def update_bizcontacts(uuid: str, update_data: BizContactsUpdateModel, db: AsyncSession = Depends(get_db),):
    updated_data = await update_bizcontacts_data_as_uuid(uuid, db, update_data.dict(exclude_unset=True))
    return {"Message": "Bizinfo Updated Successfully", "Updated Data": updated_data}

# uuid 조회
@router.get("/uuid/{uuid}", summary="기업 광고 정보 검색", status_code=status.HTTP_201_CREATED, response_model=BizContactsDataResponse)
async def search_bizcontacts(uuid: str, db: AsyncSession = Depends(get_db)):#, current_user: dict = Depends(get_current_user)): # 인증 종속성 추가
    try:
        result = await search_bizcontacts_data_from_DB_as_uuid(uuid, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# uuid 삭제
@router.delete("/uuid/{uuid}", summary="기업 광고 정보 삭제", status_code=status.HTTP_201_CREATED)
async def delete_bizcontacts(uuid:str, db: AsyncSession = Depends(get_db)):#, current_user: dict = Depends(get_current_user)):
    try:
        result = await delete_bizcontacts_data_from_DB_as_uuid(uuid, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# order_id 수정
@router.put("/{order_id}")
async def update_bizcontacts(order_id: int, update_data: BizContactsUpdateModel, db: AsyncSession = Depends(get_db),):
    updated_data = await update_bizcontacts_data(order_id, db, update_data.dict(exclude_unset=True))
    return {"Message": "Bizinfo Updated Successfully", "Updated Data": updated_data}

# order_id 조회
@router.get("/order_id/{order_id}", summary="기업 광고 정보 검색", status_code=status.HTTP_201_CREATED, response_model=BizContactsDataResponse)
async def search_bizcontacts(order_id: int, db: AsyncSession = Depends(get_db)):#, current_user: dict = Depends(get_current_user)): # 인증 종속성 추가
    try:
        result = await search_bizcontacts_data_from_DB(order_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
# order_id 삭제
@router.delete("/order_id/{order_id}", summary="기업 광고 정보 삭제", status_code=status.HTTP_201_CREATED)
async def delete_bizcontacts(order_id:int, db: AsyncSession = Depends(get_db)):#, current_user: dict = Depends(get_current_user)):
    try:
        result = await delete_bizcontacts_data_from_DB(order_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
