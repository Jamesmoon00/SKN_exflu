from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.biz_info import BizInfoDataRequests, BizInfoResponse
from app.services.biz_info_service import insert_bizinfo_data_to_DB, search_bizinfo_data_from_DB, delete_bizinfo_data_from_DB
from app.database.database import get_db
import json

router = APIRouter(prefix="/bizinfo", tags=["Business Infomation"])

# 기업 정보 저장 API
@router.post("/insert", summary="기업 정보 저장", status_code=status.HTTP_201_CREATED)
async def insert_bizinfo(bizinfo_data: BizInfoDataRequests, db: AsyncSession = Depends(get_db)):
    try:
        result = await insert_bizinfo_data_to_DB(bizinfo_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{biz_key}", summary="기업 정보 검색", status_code=status.HTTP_201_CREATED, response_model=BizInfoResponse)
async def search_bizinfo(biz_key: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_bizinfo_data_from_DB(biz_key, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{biz_key}", summary="기업 정보 삭제", status_code=status.HTTP_201_CREATED)
async def delete_bizinfo(biz_key:int, db: AsyncSession = Depends(get_db)):
    try:
        result = await delete_bizinfo_data_from_DB(biz_key, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
