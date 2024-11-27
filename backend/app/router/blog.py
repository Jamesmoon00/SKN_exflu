from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.blog import TitleCreate, BlogContent
from app.services.blog_service import send_title_data_to_DB, send_blog_content_data_to_DB
from app.database.database import get_db

router = APIRouter(prefix="/blog", tags=["blog"])

# 블로그 제목 저장 API
@router.post("/title", status_code=status.HTTP_201_CREATED)
async def create_title(title_data: TitleCreate, db: AsyncSession = Depends(get_db)):
    try:
        result = await send_title_data_to_DB(title_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.post("/blog/content")
async def upload_blog(blog: BlogContent , db: AsyncSession = Depends(get_db)): # ,image_data: Optional[UploadFile] =File(None)
    try:
        result = await send_blog_content_data_to_DB(blog, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
