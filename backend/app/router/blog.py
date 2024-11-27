from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.blog import TitleCreate, BlogContent
from app.services.blog_service import send_title_data_to_DB, process_blog_data
from app.database.database import get_db
import json

router = APIRouter(prefix="/blog", tags=["Blog"])

# 블로그 제목 저장 API
@router.post("/title", status_code=status.HTTP_201_CREATED)
async def create_title(title_data: TitleCreate, db: AsyncSession = Depends(get_db)):
    try:
        result = await send_title_data_to_DB(title_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/content")
async def send_blog_content_data_to_DB(
    blog: str = Form(...),  # JSON 데이터 문자열
    images: list[UploadFile] = File(...),  # 파일 리스트
    db: AsyncSession = Depends(get_db),  # DB 세션
):
    try:
        # JSON 파싱
        blog_data = json.loads(blog)
        blog_content = BlogContent(**blog_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="Invalid JSON format")
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Validation Error: {e}")

    # 비즈니스 로직 처리
    result = await process_blog_data(blog_content, images, db)
    return result
