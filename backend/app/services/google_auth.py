# app/services/google_auth.py
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.database import get_db
from app.database.models import User
from app.auth.oauth import oauth
from app.auth.token import create_access_token, create_refresh_token

async def google_login_redirect(request):
    """
    구글 로그인 리다이렉션 URL 생성
    """
    redirect_uri = "https://www.jamesmoon.click/auth/google/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

async def handle_google_callback(request, db: AsyncSession):
    # Google에서 토큰 및 사용자 정보 가져오기
    token = await oauth.google.authorize_access_token(request)
    user_info = token.get("userinfo")
    
    if not user_info:
        # Google People API를 사용해 사용자 정보 가져오기
        user_info = await oauth.google.parse_id_token(request, token)

    if not user_info:
        raise HTTPException(status_code=400, detail="Google login failed")

    # 사용자 정보 가져오기 (누락된 필드에 기본값 설정)
    email = user_info.get("email")
    name = user_info.get("name", "Unknown User")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email not found in user info")

    # 데이터베이스에서 사용자 검색 또는 생성
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar()

    if not user:
        user = User(email=email, name=name)
        db.add(user)
        await db.commit()
        await db.refresh(user)

    # Access/Refresh Token 생성
    access_token = create_access_token(data={"sub": user.email})
    refresh_token = create_refresh_token(data={"sub": user.email})

    # Refresh Token 저장
    user.refresh_token = refresh_token
    await db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

