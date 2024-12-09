from fastapi import APIRouter
from app.common.config import kakao_id, kakao_redirect_url, kakao_pwd
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import FastAPI, Request, Response, Depends, HTTPException, Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.future import select
from app.database.database import get_db
from app.auth.token import create_access_token, create_refresh_token
from app.auth.oauth import oauth
from app.database.models import User
from app.logger import logger

# 라우터 생성
router = APIRouter(tags=["kakao login"])

# Kakao OAuth 정보
CLIENT_ID = kakao_id
REDIRECT_URI = kakao_redirect_url

# Jinja2 템플릿 디렉토리 설정
templates = Jinja2Templates(directory="templates")

@router.get("/auth/kakao")
async def login_kakao():
    """
    Kakao OAuth URL로 리디렉션
    """
    kakao_oauth_url = (
        f"https://kauth.kakao.com/oauth/authorize"
        f"?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
    )
    # RedirectResponse를 사용하여 리디렉션 응답 생성
    return RedirectResponse(url=kakao_oauth_url)

# Kakao Callback 처리 함수
@router.get("/auth/kakao/callback", response_class=HTMLResponse)
async def handle_kakao_callback(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        # Step 1: Kakao에서 Access Token 및 사용자 정보 가져오기
        token = await oauth.kakao.authorize_access_token(request)
        if not token:
            logger.error("Failed to authorize Kakao access token")
            raise HTTPException(status_code=400, detail="Failed to authorize access token")
        
        user_info_response = await oauth.kakao.get("https://kapi.kakao.com/v2/user/me", token=token)
        if not user_info_response:
            logger.error("Failed to fetch Kakao user info")
            raise HTTPException(status_code=400, detail="Failed to fetch user info")
        
        user_info = user_info_response.json()
        logger.info(f"Kakao user info: {user_info}")

        # Step 2: 사용자 정보 가져오기
        kakao_id = user_info.get("id")  # 고유 ID
        kakao_account = user_info.get("kakao_account", {})
        email = kakao_account.get("email")
        name = user_info.get("properties", {}).get("nickname", "Unknown User")

        # 이메일이 없는 경우 대체값 생성 (예: kakao_id 기반 임시 이메일 생성)
        if not email:
            email = f"{kakao_id}@kakao.com"  # 고유 ID 기반의 임시 이메일

        if not email:
            logger.error("Email not found in Kakao user info")
            raise HTTPException(status_code=400, detail="Email not found in Kakao user info")

        # Step 3: 데이터베이스에서 사용자 검색 또는 생성
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            # 새로운 사용자 생성
            user = User(email=email, name=name, kakao_id=kakao_id)
            db.add(user)
            await db.commit()
            await db.refresh(user)

        # Step 4: Access/Refresh Token 생성
        provider = "kakao"  # Kakao 로그인이므로 provider를 "kakao"로 설정
        access_token = create_access_token(data={"sub": user.email}, provider=provider)
        refresh_token = create_refresh_token(data={"sub": user.email}, provider=provider)

        # Refresh Token 저장
        user.refresh_token = refresh_token
        await db.commit()

        # Step 5: RedirectResponse로 리디렉트 처리
        redirect_url = "https://www.jamesmoon.click/contact"  # 리디렉션할 URL
        response = RedirectResponse(url=redirect_url, status_code=302)
        response.set_cookie(
            key="access_token", value=access_token, httponly=True, samesite="Lax", secure=False
        )
        response.set_cookie(
            key="refresh_token", value=refresh_token, httponly=True, samesite="Lax", secure=False
        )
        logger.info(f"Kakao login successful for user: {email}")
        return response

    except Exception as e:
        logger.error(f"Exception in Kakao callback: {e}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")