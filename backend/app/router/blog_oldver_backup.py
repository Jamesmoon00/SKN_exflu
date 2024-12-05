from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.blog import CommentDelete, TitleCreate, BlogContent, CommentCreate, CommentResponse, BlogCommentCountReapone
from app.services.blog_service import view_all_blog_data_from_DB, send_title_data_to_DB, process_blog_data, get_blog_data_from_DB, create_comment_content, get_comments_contents, delete_comment_data, delete_blog_from_DB, add_like_on_blog_page, get_comments_count_from_DB
from app.database.database import get_db
import json

router = APIRouter(prefix="/blog", tags=["Blog"])

# 블로그 전체 조회
@router.get("/", summary="블로그 전체 불러오기")
async def get_blog_data(db: AsyncSession = Depends(get_db)):
    try:
        result = await view_all_blog_data_from_DB(db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 블로그 제목 저장 API
@router.post("/title", summary="블로그 제목 저장", status_code=status.HTTP_201_CREATED)
async def create_title(title_data: TitleCreate, db: AsyncSession = Depends(get_db)):
    try:
        result = await send_title_data_to_DB(title_data, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 블로그 내용 저장
@router.post("/contents", summary="블로그 내용 저장")
async def send_blog_content_data_to_DB(
    blog: str = Form(...),  # JSON 데이터 문자열
    images: Optional[list[UploadFile]] = File(None),  # 파일 리스트
    db: AsyncSession = Depends(get_db),  # DB 세션
):
    try:
        # JSON 파싱
        blog_data = json.loads(blog)
        print(blog_data)
        blog_content = BlogContent(**blog_data)
    except json.JSONDecodeError:
        raise HTTPException(status_code=422, detail="Invalid JSON format")
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Validation Error: {e}")

    # 비즈니스 로직 처리
    result = await process_blog_data(blog_content, images, db)
    return result

# 블로그 삭제
@router.delete("/{post_id}", summary="블로그 글 삭제", response_model=dict)
async def delete_blog(post_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await delete_blog_from_DB(post_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 블로그 전체 내용 확인
@router.get("/{post_id}", summary="블로그 제목, 글 내용 불러오기 + 조회수 상승")
async def get_blog_data(post_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await get_blog_data_from_DB(post_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 블로그 글 좋아요
@router.post("/{post_id}/like", summary="블로그 좋아요", response_model=dict)
async def add_like(post_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await add_like_on_blog_page(post_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 블로그 댓글 갯수
@router.get("/{post_id}/comments_count", summary="블로그 글의 댓글 수 조회", response_model=dict)
async def get_comments_count(post_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await get_comments_count_from_DB(post_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 댓글 작성
@router.post("/comments", summary="블로그 댓글 작성", response_model=CommentResponse)
async def create_comment(comment: CommentCreate, db: AsyncSession = Depends(get_db)):
    try:
        result = await create_comment_content(comment, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 댓글 조회(송수신)
@router.get("/comments/{post_id}", summary="블로그 댓글 조회", response_model=list[CommentResponse])
async def get_comments(post_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await get_comments_contents(post_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 댓글 삭제
@router.delete("/comments/{post_id}", summary="블로그 댓글 삭제", response_model=dict)
async def delete_comment(comment: CommentDelete, db: AsyncSession = Depends(get_db)):
    try:
        result = await delete_comment_data(comment, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



