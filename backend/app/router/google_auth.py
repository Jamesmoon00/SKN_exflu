# app/router/google_auth.py
from fastapi import APIRouter, Depends, Request, HTTPException, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt, JWTError
from app.database.database import get_db
from app.services.google_auth import google_login_redirect, handle_google_callback
from app.auth.token import SECRET_KEY, ALGORITHM, create_access_token

router = APIRouter(tags=["google login"])

@router.get("/auth/google")
async def google_login(request: Request):
    """
    구글 로그인 시작
    """
    return await google_login_redirect(request)

@router.get("/auth/google/callback")
async def google_callback(request: Request, db: AsyncSession = Depends(get_db)):
    """
    구글 로그인 콜백
    """
    return await handle_google_callback(request, db)


@router.post("/auth/refresh", summary="새 Access Token 발급")
async def refresh_access_token(refresh_token: str = Cookie(None)):
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh Token not found in cookies.")

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email = payload.get("sub")
        if not user_email:
            raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")

        # 새 Access Token 생성
        new_access_token = create_access_token(data={"sub": user_email})
        return {"access_token": new_access_token, "token_type": "bearer"}
    except JWTError:
        raise HTTPException(status_code=401, detail="Refresh Token이 만료되었거나 유효하지 않습니다.")
