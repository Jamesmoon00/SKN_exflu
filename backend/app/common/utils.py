import mimetypes
from fastapi import UploadFile, HTTPException
from passlib.context import CryptContext
from app.common.config import s3_client
from app.common.consts import BUCKET_NAME, REGION_NAME
import uuid

# 유효한 MIME 타입 및 확장자 정의
VALID_MIME_TYPES = {"application/json", "image/png", "image/jpeg"}
VALID_EXTENSIONS = {".json", ".png", ".jpg", ".jpeg"}  # .jpg와 .jpeg 추가

def is_valid_file_type(file: UploadFile):
    # MIME 타입 검증
    mime_type, _ = mimetypes.guess_type(file.filename)
    if mime_type not in VALID_MIME_TYPES:
        return False
    # 확장자 검증
    if not file.filename.lower().endswith(tuple(VALID_EXTENSIONS)):
        return False
    return True

def make_pwd_to_hash():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context

async def upload_image_to_s3(file: UploadFile) -> str:
    """
    AWS S3에 이미지를 업로드하고 URL을 반환합니다.
    """
    try:
        file_extension = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        s3_key = f"blog_images/{unique_filename}"
        
        # S3에 파일 업로드
        s3_client.upload_fileobj(
            file.file,
            BUCKET_NAME,
            s3_key,
            ExtraArgs={"ContentType": file.content_type}
        )

        # 업로드된 파일의 URL 생성
        s3_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
        return s3_url

    except Exception as e:
        print(f"Error uploading image to S3: {e}")
        raise HTTPException(status_code=500, detail="Failed to upload image")
    
    
def create_uuid():
    # UUID1 생성
    uuid1 = uuid.uuid1()
    return uuid1