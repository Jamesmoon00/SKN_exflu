# app/router/google_auth.py
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.database import get_db
from app.services.google_auth import google_login_redirect, handle_google_callback

router = APIRouter(tags=["login"])

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
