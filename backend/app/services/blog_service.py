from app.schemas.blog import TitleCreate
from app.database.models import BlogPost, ContentBlock
from typing import Optional
from app.common.consts import BUCKET_NAME, REGION_NAME
from app.common.config import s3_client
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.common.utils import is_valid_file_type
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

'''
아래 process_blog_data에 입력하기 위한 string 셋은 아래와 같아

{
  "post_id": 1,
  "blocks": [
    {"block_type": "text", "content": "This is a text block", "block_order": 0},
    {"block_type": "image", "content": "image1", "block_order": 1},
    {"block_type": "text", "content": "This is another text block", "block_order": 2},
    {"block_type": "image", "content": "image2", "block_order": 3}
  ]
}


왜 이렇게 string으로 처리해야 하는가?

1. 파일 업로드 기능이 있어서 application/json으로 인식하지 않고 multipart/form-data로 인식함
2. 라우터에서 인식된 input은 string의 형식을 가지므로 라우터에서 json으로 변환이 필요하다
3. 그렇다면 input으로 넣는 string에서 미리 json에 맞게 데이터를 넣어줘야 한다.
4. 따라서 위와 같은 형식의 글이 작성되게 된다.
5. 위의 post_id에는 제목이 들어가게 된다.
'''

async def process_blog_data(blog, image_data_list, db: AsyncSession):
    try:
        # 기존 BlogPost 확인 및 업데이트
        existing_blog_post = await db.execute(
            select(BlogPost).where(BlogPost.post_id == blog.post_id)
        )
        existing_blog_post = existing_blog_post.scalar_one_or_none()

        if existing_blog_post:
            # 기존 글 수정
            existing_blog_post.title = f"Blog {blog.post_id}"  # 필요한 필드만 업데이트
            new_blog_post = existing_blog_post
        else:
            # 새로운 글 생성
            new_blog_post = BlogPost(title=f"Blog {blog.post_id}")
            db.add(new_blog_post)
            await db.flush()

        # 이미지 파일 인덱스
        image_index = 0

        for block in blog.blocks:
            if block.block_type == "text":
                # 텍스트 블록 처리
                new_block = ContentBlock(
                    post_id=new_blog_post.post_id,
                    block_type="text",
                    content=block.content,
                    block_order=block.block_order,
                )
                db.add(new_block)
            elif block.block_type == "image":
                # 이미지 블록 처리
                if image_index >= len(image_data_list):
                    raise HTTPException(status_code=400, detail=f"Image file missing for block {block.block_order}")
                
                # S3 업로드
                image_file = image_data_list[image_index]
                image_index += 1
                
                # 파일 검증
                if not is_valid_file_type(image_file):
                    raise HTTPException(
                        status_code=400,
                        detail=f"Invalid file type for block {block.block_order}. Only JPG or PNG files are allowed.",
                    )
                
                # S3 업로드
                s3_key = f"blogs/{new_blog_post.post_id}/{block.block_order}.png"
                s3_client.upload_fileobj(image_file.file, BUCKET_NAME, s3_key)
                s3_url = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{s3_key}"
                
                # 블록 저장
                new_block = ContentBlock(
                    post_id=new_blog_post.post_id,
                    block_type="image",
                    content=s3_url,
                    block_order=block.block_order,
                )
                db.add(new_block)

        await db.commit()
        return {"message": "Blog saved successfully", "blog_id": new_blog_post.post_id}
    except Exception as e:
        print(f"Error in process_blog_data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")