from app.schemas.blog import TitleCreate, BlogContent
from app.database.models import BlogPost, ContentBlock
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
# from app.common.config import get_s3_client
# # AWS S3 클라이언트
# s3_client = get_s3_client()

async def send_title_data_to_DB(title_data: TitleCreate, db: AsyncSession):
    new_title = BlogPost(title=title_data.title)
    try:
        # 데이터베이스에 새 레코드 추가
        db.add(new_title)
        await db.commit()
        await db.refresh(new_title)
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Failed to save title"
        )
    return {"id": new_title.post_id, "title": new_title.title, "created_at": new_title.created_at}

async def send_blog_content_data_to_DB(blog: BlogContent , db: AsyncSession): # ,image_data: Optional[UploadFile] =File(None)
    # print(f"Received blog data: {blog}")  # 추가된 로그
    # print(f"Database session: {db}")  # db 세션 확인
    # 블로그 포스트 저장
    if not blog.blocks:  # 블록이 비어있는지 확인
        raise HTTPException(status_code=400, detail="No blocks provided")
    try:
        for idx, block in enumerate(blog.blocks):
            if block.block_type == "text":
                new_block = ContentBlock(
                    post_id=blog.post_id,
                    block_type=block.block_type,  # 반복문 내에서 block.block_type로 접근
                    content=block.content,        # 반복문 내에서 block.content로 접근
                    block_order=idx               # 반복문 내에서 idx 사용
                )
                db.add(new_block)
                await db.flush()  # DB에 추가된 상태 유지
                await db.refresh(new_block)  # 새 블록의 상태 갱신
        await db.commit()
    except Exception as e:
        await db.rollback()  # 오류 발생 시 롤백
        raise HTTPException(status_code=500, detail=f"Failed to save blog blocks: {e}")
    return {"post_id":new_block.post_id,
            "block_type":new_block.block_type,  # 반복문 내에서 block.block_type로 접근
            "content":new_block.content,        # 반복문 내에서 block.content로 접근
            "block_order":new_block.block_order}

            # elif block.block_type == "image":
            #     try:
            #         # Base64 디코딩 및 S3 업로드
            #         # image_data = base64.b64decode(block.content)  # Base64 디코딩
            #         file_name = f"blog/{blog.post_id}/{idx}.png"  # S3에 저장할 경로
            #         s3_client.put_object(
            #             Bucket=BUCKET_NAME,
            #             Key=file_name,
            #             Body=image_data,
            #             ContentType="image/png",
            #         )

            #         # S3 URL 생성
            #         image_url = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{file_name}"

            #         # 데이터베이스에 저장
            #         new_block = models.ContentBlock(
            #             post_id=blog.post_id,
            #             block_type=block.block_type,
            #             content=image_url,  # S3 URL 저장
            #             block_order=idx,
            #         )
            #         db.add(new_block)
            #     except (NoCredentialsError, PartialCredentialsError) as e:
            #         raise HTTPException(status_code=500, detail="S3 credentials error")
            #     except Exception as e:
            #         raise HTTPException(status_code=500, detail=f"Failed to upload image: {e}")
