# app/auth/oauth.py
import os
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv
from app.common.config import get_parameter

load_dotenv()  # .env 파일에서 환경 변수 로드

oauth = OAuth()
oauth.register(
    name="google",
    client_id=get_parameter("/MYAPP/GOOGLE/AUTH/NAME"),
    client_secret=get_parameter("/MYAPP/GOOGLE/AUTH/PWD"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
    redirect_uri="https://backdocsend.jamesmoon.click/auth/google/callback"  # 정확히 Google Console에 등록된 리디렉션 URL과 일치
)
oauth.register(
    name='kakao',
    client_id=get_parameter("/MYAPP/KAKAO/AUTH/NAME"),
    client_secret=get_parameter("/MYAPP/KAKAO/AUTH/PWD"),
    access_token_url="https://kauth.kakao.com/oauth/token",
    authorize_url="https://kauth.kakao.com/oauth/authorize",
    client_kwargs={"scope": "profile"},
    api_base_url="https://kapi.kakao.com/v2/user/me"
)