from fastapi import APIRouter, Depends, HTTPException
from typing import Any, Dict, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.exaone import PromptRequest
from app.services.exaone_service import generate_ollama_exaone_service
from app.database.database import get_db
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/exaone", tags=["exaone"])

# 블로그 전체 조회
@router.post("/generate", summary="Ollama 송수신")
def generate_ollama_exaone(request: PromptRequest):
    """
    클라이언트의 프롬프트를 Ollama 서버에 전달하고 스트리밍 데이터를 반환합니다.
    """
    try:
        payload = {"model": request.model, "prompt": request.prompt}
        return StreamingResponse(generate_ollama_exaone_service(payload), media_type="text/plain")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    