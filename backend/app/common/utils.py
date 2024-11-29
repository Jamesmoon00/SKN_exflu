import mimetypes
from fastapi import UploadFile, HTTPException
from passlib.context import CryptContext


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