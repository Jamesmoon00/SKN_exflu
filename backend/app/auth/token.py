# app/auth/token.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.common.config import get_parameter
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

SECRET_KEY = get_parameter("/MYAPP/GOOGLE/AUTH/SECRETKEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/google")  # 로그인 엔드포인트

# 토큰을 검증하고 유저 정보를 추출
def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get("exp")
        if exp and datetime.utcnow().timestamp() > exp:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_access_token(token)
        user_email = payload.get("sub")
        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="사용자 정보를 확인할 수 없습니다. 다시 로그인하세요.",
            )
        return user_email
    except HTTPException as e:
        # 토큰 만료 예외 처리
        if e.status_code == status.HTTP_401_UNAUTHORIZED:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="토큰이 만료되었습니다. Refresh Token을 사용하여 새 Access Token을 요청하세요.",
                headers={"WWW-Authenticate": "Bearer"},  # 클라이언트가 이 헤더를 확인 가능
            )
        raise e
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 토큰입니다.",
        )

def create_access_token(data: dict):
    """
    Access Token 생성
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    """
    Refresh Token 생성
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
