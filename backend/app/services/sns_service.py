from app.schemas.sns import TitleCreate, CommentResponse,CommentCreate
from app.database.models import SNSPost, ContentBlockForSNS, SNSComment
from typing import Optional
from app.common.consts import BUCKET_NAME, REGION_NAME
from app.common.config import s3_client
from app.common.utils import make_pwd_to_hash
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from app.common.utils import is_valid_file_type
from passlib.context import CryptContext
from sqlalchemy.orm import selectinload

pwd_context = make_pwd_to_hash()
# from app.common.config import get_s3_client
# # AWS S3 클라이언트
# s3_client = get_s3_client()


async def view_all_sns_data_from_DB(db: AsyncSession):
    """
    데이터베이스에서 모든 BlogPost 데이터를 검색하고, 관련된 ContentBlock 및 BlogComment 데이터를 함께 반환합니다.
    """
    try:
        # 1. BlogPost, ContentBlock, BlogComment를 모두 로드
        blog_posts_query = await db.execute(
            select(SNSPost)
            .options(
                selectinload(SNSPost.blocks),        # ContentBlock 미리 로드
                selectinload(SNSPost.comments)       # BlogComment 미리 로드
            )
        )
        blog_posts = blog_posts_query.scalars().all()

        # 2. BlogPost가 존재하지 않을 경우 빈 리스트 반환
        if not blog_posts:
            return []

        # 3. 데이터 변환 (JSON 형태로 반환)
        response_data = [
            {
                "post_id": blog_post.post_id,
                "title": blog_post.title,
                "created_at": blog_post.created_at,
                "views": blog_post.views,
                "likes": blog_post.likes,
                "is_ad": blog_post.is_ad,
                "comments_count": blog_post.comments_count,
                "blocks": [
                    {
                        "block_type": block.block_type,
                        "content": block.content,
                        "block_order": block.block_order,
                    }
                    for block in blog_post.blocks  # 미리 로드된 blocks 사용
                ],
                "comments": [
                    {
                        "comment_id": comment.comment_id,
                        "post_id": comment.post_id,
                        "comment_name": comment.comment_name,
                        "comment_content": comment.comment_content,
                        "created_at": comment.created_at,
                    }
                    for comment in blog_post.comments  # 미리 로드된 comments 사용
                ],
            }
            for blog_post in blog_posts
        ]

        # 4. 반환 데이터
        return response_data

    except Exception as e:
        # 기타 예상치 못한 에러 처리
        print(f"Error in view_all_blog_data_from_DB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def send_title_data_to_DB(title_data: TitleCreate, db: AsyncSession):
    new_title = SNSPost(title=title_data.title)
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

async def process_sns_data(sns, image_data_list, db: AsyncSession):
    '''
    아래 process_sns_data에 입력하기 위한 string 셋은 아래와 같아

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
    try:
        # 기존 SNSPost 확인 및 업데이트
        existing_sns_post = await db.execute(
            select(SNSPost).where(SNSPost.post_id == sns.post_id)
        )
        existing_sns_post = existing_sns_post.scalar_one_or_none()

        if existing_sns_post:
            # 기존 글 수정
            new_sns_post = existing_sns_post
        else:
            # 새로운 글 생성
            new_sns_post = SNSPost(title=f"sns {sns.post_id}")
            db.add(new_sns_post)
            await db.flush()

        # 이미지 파일 인덱스
        image_index = 0

        for block in sns.blocks:
            if block.block_type == "text":
                # 텍스트 블록 처리
                new_block = ContentBlockForSNS(
                    post_id=new_sns_post.post_id,
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
                s3_key = f"sns/{new_sns_post.post_id}/{block.block_order}.png"
                s3_client.upload_fileobj(image_file.file, BUCKET_NAME, s3_key)
                s3_url = f"https://{BUCKET_NAME}.s3.{REGION_NAME}.amazonaws.com/{s3_key}"
                
                # 블록 저장
                new_block = ContentBlockForSNS(
                    post_id=new_sns_post.post_id,
                    block_type="image",
                    content=s3_url,
                    block_order=block.block_order,
                )
                db.add(new_block)

        await db.commit()
        return {"message": "sns saved successfully", "sns_id": new_sns_post.post_id}
    except Exception as e:
        print(f"Error in process_sns_data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

async def get_sns_data_from_DB(post_id: str, db: AsyncSession):
    """
    title로 SNSPost를 검색하고, 저장된 데이터를 반환합니다.
    """
    try:
        # 1. SNSPost에서 title로 검색
        sns_post_query = await db.execute(select(SNSPost).where(SNSPost.post_id == post_id))
        sns_post = sns_post_query.scalars().all()

        # 2. SNSPost가 존재하지 않을 경우 에러 반환
        if not sns_post:
            raise HTTPException(status_code=404, detail=f"sns with title '{post_id}' not found.")
        
        sns_post = sns_post[0]
        sns_post.views += 1
        await db.commit()
        
        # 댓글 갯수 계산
        comments_count_result = await db.execute(
        select(func.count(SNSComment.comment_id)).where(SNSComment.post_id == post_id)
    )
        comments_count = comments_count_result.scalar()
        
        # 3. 해당 post_id로 ContentBlockForSNS 검색
        content_blocks_query = await db.execute(
            select(ContentBlockForSNS).where(ContentBlockForSNS.post_id == sns_post.post_id).order_by(ContentBlockForSNS.block_order)
        )
        content_blocks = content_blocks_query.scalars().all()

        # 4. 데이터 변환 (JSON 형태로 반환할 수 있도록 구조화)
        response_data = {
            "post_id": sns_post.post_id,
            "title": sns_post.title,
            "created_at": sns_post.created_at,
            "views": sns_post.views,
            "likes": sns_post.likes,
            "is_ad": sns_post.is_ad,
            "comments_count": sns_post.comments_count,
            "blocks": [
                {
                    "block_type": block.block_type,
                    "content": block.content,
                    "block_order": block.block_order,
                }
                for block in content_blocks
            ],
        }

        # 5. 반환 데이터
        return response_data

    except HTTPException as http_ex:
        # HTTPException 처리 (FastAPI가 클라이언트에 반환)
        raise http_ex
    except Exception as e:
        # 기타 예상치 못한 에러 처리
        print(f"Error in get_sns_data: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

async def add_like_on_sns_page(post_id: int, db: AsyncSession):
    """
    특정 SNS 글에 추천 추가
    """
    # SNS 글 가져오기
    sns_query = await db.execute(select(SNSPost).where(SNSPost.post_id == post_id))
    sns = sns_query.scalar_one_or_none()

    if not sns:
        raise HTTPException(status_code=404, detail="sns not found")

    # 추천수 증가
    sns.likes += 1
    await db.commit()

    return {
        "post_id": sns.post_id,
        "title": sns.title,
        "likes": sns.likes
    }

async def delete_sns_from_DB(post_id: str, db: AsyncSession):
    """
    SNS와 관련된 모든 데이터를 삭제
    """
    # 1. SNS 글 존재 확인
    sns_query = await db.execute(select(SNSPost).where(SNSPost.post_id == post_id))
    sns = sns_query.scalar_one_or_none()

    if not sns:
        raise HTTPException(status_code=404, detail="sns not found")

    # 2. SNS 삭제
    await db.delete(sns)
    await db.commit()

    return {"message": f"sns with post_id {post_id} and its comments deleted successfully"}
async def create_comment_content(comment: CommentCreate, db: AsyncSession):
    """
    댓글 생성 및 블로그 글의 댓글 수 증가
    """
    # 비밀번호 암호화
    hashed_password = pwd_context.hash(comment.comment_password)

    # 댓글 생성
    new_comment = SNSComment(
        post_id=comment.post_id,
        comment_name=comment.comment_name,
        comment_password=hashed_password,  # 암호화된 비밀번호 저장
        comment_content=comment.comment_content,
    )
    db.add(new_comment)

    # 댓글 수 증가
    blog_query = await db.execute(select(SNSPost).where(SNSPost.post_id == comment.post_id))
    blog = blog_query.scalar_one_or_none()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog post not found")
    blog.comments_count += 1

    await db.commit()
    await db.refresh(new_comment)

    # Pydantic 모델로 직렬화된 데이터 반환
    return {
        "message": "Comment added successfully",
        "comments_count": blog.comments_count,
        "comment_id": new_comment.comment_id,
        "post_id": new_comment.post_id,
        "comment_name": new_comment.comment_name,
        "comment_content": new_comment.comment_content,
    }
    
async def get_comments_contents(post_id: int, db: AsyncSession):
    """
    특정 글의 댓글 조회
    """
    comments_query = await db.execute(select(SNSComment).where(SNSComment.post_id == post_id))
    comments = comments_query.scalars().all()

    return comments

async def get_comments_count_from_DB(post_id: int, db: AsyncSession):
    
    """
    특정 글의 댓글 갯수 조회
    """
    # 댓글 갯수 계산
    result = await db.execute(
        select(func.count(SNSComment.comment_id)).where(SNSComment.post_id == post_id)
    )
    comments_count = result.scalar()

    return {"post_id": post_id, "comments_count": comments_count}

async def delete_comment_data(post_id: int, comment_name: str, comment_password: str, db: AsyncSession):
    """
    댓글 삭제
    """
    # 댓글 존재 확인 (post_id와 comment_name 모두 확인)
    comment_query = await db.execute(
        select(SNSComment).where(
            SNSComment.post_id == post_id,
            SNSComment.comment_name == comment_name
        )
    )
    comment = comment_query.scalar_one_or_none()

    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    # 비밀번호 검증
    if not pwd_context.verify(comment_password, comment.comment_password):
        raise HTTPException(status_code=403, detail="Invalid password")

    # 댓글 삭제
    await db.delete(comment)

    # 댓글 수 감소
    blog_query = await db.execute(select(SNSPost).where(SNSPost.post_id == post_id))
    blog = blog_query.scalar_one_or_none()
    if blog:
        blog.comments_count -= 1

    await db.commit()

    return {"message": "Comment deleted successfully"}