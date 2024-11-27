from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional, Union, Literal, Annotated
from app.services.core_service import search_categories_from_DB, search_products_from_DB, search_specifications_laptop_from_DB, search_specifications_smartphone_from_DB, search_specifications_tabletpc_from_DB
from app.database.database import get_db
from app.schemas.core import CategoryRequest, ProductRequest, SpecificationsBase

router = APIRouter(tags=["Database"])

@router.post("/productcategories", 
    summary="Get product categories",
    status_code=status.HTTP_200_OK,)
async def search_categories(request: CategoryRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_categories_from_DB(request, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products",
    summary="Get products",
    status_code=status.HTTP_200_OK,)
async def search_products(request: ProductRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_products_from_DB(request, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/specifications_laptop", 
    summary="Get products of laptop spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def search_specifications_laptop(request: ProductRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_specifications_laptop_from_DB(request, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/specifications_smartphone", 
    summary="Get products of smartphone spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def search_specifications_smartphone(request: ProductRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_specifications_smartphone_from_DB(request, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/specifications_tabletpc", 
    summary="Get products of tabletpc spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def search_specifications_tabletpc(request: ProductRequest, db: AsyncSession = Depends(get_db)):
    try:
        result = await search_specifications_tabletpc_from_DB(request, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


