from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.biz_info import BizInfoDataRequests, BizInfoResponse
from app.services.biz_info_service import insert_bizinfo_data_to_DB, search_bizinfo_data_from_DB, delete_bizinfo_data_from_DB, search_all_bizinfo_data_from_DB
from app.database.database import get_db
from app.auth.token import get_current_user  # 인증 함수
import json
import logging

router = APIRouter(prefix="/bizinfo", tags=["Business Infomation"])

@router.post("/", summary="기업 정보 전체 조회", status_code=status.HTTP_201_CREATED)
async def insert_bizinfo(db: AsyncSession = Depends(get_db)):
# async def insert_bizinfo(bizinfo_data: BizInfoDataRequests, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        result = await search_all_bizinfo_data_from_DB(db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 기업 정보 저장 API
@router.post("/insert", summary="기업 정보 저장", status_code=status.HTTP_201_CREATED)
async def insert_bizinfo(bizinfo_data: BizInfoDataRequests, db: AsyncSession = Depends(get_db)):
    logging.info(f"Request data: {bizinfo_data.json()}")
# async def insert_bizinfo(bizinfo_data: BizInfoDataRequests, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        result = await insert_bizinfo_data_to_DB(bizinfo_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{biz_key}", summary="기업 정보 검색", status_code=status.HTTP_201_CREATED, response_model=BizInfoResponse)
async def search_bizinfo(biz_key: int, db: AsyncSession = Depends(get_db)):  # 인증 종속성 추가
# async def search_bizinfo(biz_key: int, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):  # 인증 종속성 추가
    try:
        result = await search_bizinfo_data_from_DB(biz_key, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{biz_key}", summary="기업 정보 삭제", status_code=status.HTTP_201_CREATED)
async def delete_bizinfo(biz_key:int, db: AsyncSession = Depends(get_db)):
# async def delete_bizinfo(biz_key:int, db: AsyncSession = Depends(get_db), current_user: str = Depends(get_current_user)):
    try:
        result = await delete_bizinfo_data_from_DB(biz_key, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
