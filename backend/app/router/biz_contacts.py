from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.biz_contacts import BizContactsDataRequests, BizContactsDataResponce
from app.services.biz_contacts_service import insert_bizcontacts_data_to_DB, search_bizcontacts_data_from_DB, delete_bizcontacts_data_from_DB
from app.database.database import get_db
from app.auth.token import get_current_user  # 인증 함수
import json

router = APIRouter(prefix="/bizcontacts", tags=["Business Contact Infomation"])

# 기업 정보 저장 API
@router.post("/insert", summary="기업 광고 정보 저장", status_code=status.HTTP_201_CREATED)
async def insert_bizcontacts(bizinfo_data: BizContactsDataRequests, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        result = await insert_bizcontacts_data_to_DB(bizinfo_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{order_id}", summary="기업 광고 정보 검색", status_code=status.HTTP_201_CREATED, response_model=BizContactsDataResponce)
async def search_bizcontacts(order_id: int, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)): # 인증 종속성 추가
    try:
        result = await search_bizcontacts_data_from_DB(order_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{order_id}", summary="기업 광고 정보 삭제", status_code=status.HTTP_201_CREATED)
async def delete_bizcontacts(order_id:int, db: AsyncSession = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        result = await delete_bizcontacts_data_from_DB(order_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
