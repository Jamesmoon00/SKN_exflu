from fastapi import APIRouter, status, HTTPException
from app.services.process_check_service import process_item
from app.schemas.process_check import ItemRequests

router = APIRouter(tags=["Check Server Connection"])

# POST 엔드포인트 정의
@router.post("/process/",
    summary="Get products of tabletpc spac by product_id",
    status_code=status.HTTP_200_OK,)
async def get_process_item(item: ItemRequests):
    try:
        result = await process_item(item)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
