# app/services/google_auth.py
from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.database import get_db
from app.database.models import User
from app.auth.oauth import oauth
from app.auth.token import create_access_token, create_refresh_token
import secrets

async def google_login_redirect(request: Request):
    """
    구글 로그인 리다이렉션 URL 생성
    """
    # Step 1: 고유한 state 생성
    state = secrets.token_urlsafe(16)
    request.session["google_state"] = state  # 세션에 state 저장

    # Step 2: 리다이렉션 URL 생성
    redirect_uri = "https://backdocsend.jamesmoon.click/auth/google/callback"
    return await oauth.google.authorize_redirect(request, redirect_uri)

async def handle_google_callback(request: Request, db: AsyncSession):
    try:
        # Step 1: state 검증
        state = request.query_params.get("state")  # 요청에서 state 값 가져오기
        saved_state = request.session.get("google_state")  # 세션에서 저장된 state 값 가져오기
        if state != saved_state:
            raise HTTPException(status_code=400, detail="Invalid state parameter")
        
        # Step 1: Google에서 토큰 및 사용자 정보 가져오기
        token = await oauth.google.authorize_access_token(request)
        if not token:
            raise HTTPException(status_code=400, detail="Failed to authorize access token")
        
        user_info = token.get("userinfo")
        
        if not user_info:
            # Google People API 사용해 사용자 정보 가져오기
            try:
                user_info = await oauth.google.parse_id_token(request, token)
            except Exception as e:
                raise HTTPException(status_code=500, detail="Failed to parse ID token")

        if not user_info:
            raise HTTPException(status_code=400, detail="Google login failed")

        # Step 2: 사용자 정보 가져오기
        email = user_info.get("email")
        name = user_info.get("name", "Unknown User")
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not found in user info")

        # Step 3: 데이터베이스에서 사용자 검색 또는 생성
        result = await db.execute(select(User).where(User.email == email))
        user = result.scalar()

        if not user:
            user = User(email=email, name=name)
            db.add(user)
            await db.commit()
            await db.refresh(user)

        # Step 4: Access/Refresh Token 생성
        access_token = create_access_token(data={"sub": user.email})
        refresh_token = create_refresh_token(data={"sub": user.email})

        # Refresh Token 저장
        user.refresh_token = refresh_token
        await db.commit()

        # Step 5: RedirectResponse로 리디렉트 처리
        redirect_url = "https://www.jamesmoon.click/contact"
        response = RedirectResponse(url=redirect_url, status_code=302)
        response.set_cookie(
            key="access_token", value=access_token, httponly=True, samesite="Lax", secure=True
        )
        response.set_cookie(
            key="refresh_token", value=refresh_token, httponly=True, samesite="Lax", secure=True
        )
        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# async def handle_google_callback(request, db: AsyncSession):
#     try:
#         # Google에서 토큰 및 사용자 정보 가져오기
#         token = await oauth.google.authorize_access_token(request)
#         if not token:
#             raise HTTPException(status_code=400, detail="Failed to authorize access token")
        
#         print("Token: ", token)
#         user_info = token.get("userinfo")
        
#         if not user_info:
#             # Google People API를 사용해 사용자 정보 가져오기
#             try:
#                 user_info = await oauth.google.parse_id_token(request, token)
#             except Exception as e:
#                 print(f"Error in parse_id_token: {e}")
#                 raise HTTPException(status_code=500, detail="Failed to parse ID token")

#         if not user_info:
#             raise HTTPException(status_code=400, detail="Google login failed")

#         # 사용자 정보 가져오기 (누락된 필드에 기본값 설정)
#         email = user_info.get("email")
#         name = user_info.get("name", "Unknown User")
        
#         if not email:
#             raise HTTPException(status_code=400, detail="Email not found in user info")

#         # 데이터베이스에서 사용자 검색 또는 생성
#         result = await db.execute(select(User).where(User.email == email))
#         user = result.scalar()

#         if not user:
#             user = User(email=email, name=name)
#             db.add(user)
#             await db.commit()
#             await db.refresh(user)

#         # Access/Refresh Token 생성
#         access_token = create_access_token(data={"sub": user.email})
#         refresh_token = create_refresh_token(data={"sub": user.email})

#         # Refresh Token 저장
#         user.refresh_token = refresh_token
#         await db.commit()

#         # RedirectResponse로 리디렉트 처리
#         redirect_url = "https://www.jamesmoon.click/contact"
#         response = RedirectResponse(url=redirect_url, status_code=302)
#         response.set_cookie(
#             key="access_token", value=access_token, httponly=True, samesite="Lax", secure=False
#         )
#         response.set_cookie(
#             key="refresh_token", value=refresh_token, httponly=True, samesite="Lax", secure=False
#         )
#         return response

#     except Exception as e:
#         print(f"Error in handle_google_callback: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# async def handle_google_callback(request, db: AsyncSession):
#     # Google에서 토큰 및 사용자 정보 가져오기
#     token = await oauth.google.authorize_access_token(request)
#     user_info = token.get("userinfo")
    
#     if not user_info:
#         # Google People API를 사용해 사용자 정보 가져오기
#         user_info = await oauth.google.parse_id_token(request, token)

#     if not user_info:
#         raise HTTPException(status_code=400, detail="Google login failed")

#     # 사용자 정보 가져오기 (누락된 필드에 기본값 설정)
#     email = user_info.get("email")
#     name = user_info.get("name", "Unknown User")
    
#     if not email:
#         raise HTTPException(status_code=400, detail="Email not found in user info")

#     # 데이터베이스에서 사용자 검색 또는 생성
#     result = await db.execute(select(User).where(User.email == email))
#     user = result.scalar()

#     if not user:
#         user = User(email=email, name=name)
#         db.add(user)
#         await db.commit()
#         await db.refresh(user)

#     # Access/Refresh Token 생성
#     access_token = create_access_token(data={"sub": user.email})
#     refresh_token = create_refresh_token(data={"sub": user.email})

#     # Refresh Token 저장
#     user.refresh_token = refresh_token
#     await db.commit()

#     # return {
#     #     "access_token": access_token,
#     #     "refresh_token": refresh_token,
#     #     "token_type": "bearer",
#     # }

#     # 리디렉트 URL 생성
#     redirect_url = "https://www.jamesmoon.click/contact"

#     # RedirectResponse로 리디렉트 처리
#     response = RedirectResponse(url=redirect_url, status_code=302)
#     response.set_cookie(key="access_token", value=access_token, httponly=True)
#     response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
#     return response

