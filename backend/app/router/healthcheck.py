from fastapi import APIRouter, HTTPException
from app.services.healthcheck_service import get_root, get_health
from app.schemas.healthcheck import HealthCheck
from fastapi import HTTPException, status

router = APIRouter(tags=["healthcheck"])

@router.get(
    "/",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def root():
    try:
        result = get_root()  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def health():
    try:
        result = get_health()  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
