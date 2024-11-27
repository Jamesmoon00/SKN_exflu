from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import ProductCategories, Products, Specifications_laptop, Specifications_smartphone, Specifications_tabletpc
from app.schemas.core import PrdCategoryBase, CategoryRequest, ProductRequest, ProductsBase, SpecificationsBase
from app.services.test_service import insert_categories_data_from_DB, upload_image
from app.database.database import get_db

router = APIRouter(tags=["Test Page"])

@router.post("/Specifications_tabletpc/", status_code=status.HTTP_201_CREATED)
async def insert_tabletpc_specification(specification: SpecificationsBase, db: AsyncSession = Depends(get_db), ):
    try:
        result = await insert_categories_data_from_DB(specification, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/upload-image-to-base64/")
async def upload_test_image(file: UploadFile = File(...)):
    try:
        result = await upload_image(file)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
