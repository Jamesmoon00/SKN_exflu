from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.core_check_service import check_categories_data_from_DB, check_products_data_from_DB, check_laptop_specificatoin_data_from_DB, check_smartphone_specificatoin_data_from_DB, check_tabletpc_specificatoin_data_from_DB
from app.database.database import get_db

router = APIRouter(tags=["Check Database"])

@router.get("/productcategories/{category_id}", 
    summary="Get product categories",
    status_code=status.HTTP_200_OK,)
async def check_categories_data(category_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await check_categories_data_from_DB(category_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products/{product_id}", 
    summary="Get products info by product_id",
    status_code=status.HTTP_200_OK,)
async def check_products_data(product_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await check_products_data_from_DB(product_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/specifications_laptop/{product_id}", 
    summary="Get products of laptop spac by product_id",
    status_code=status.HTTP_200_OK,)
async def check_laptop_specificatoin_data(product_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await check_laptop_specificatoin_data_from_DB(product_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@router.get("/specifications_smartphone/{product_id}",  
    summary="Get products of smartphone spac by product_id",
    status_code=status.HTTP_200_OK,)
async def check_smartphone_specificatoin_data(product_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await check_smartphone_specificatoin_data_from_DB(product_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/specifications_tabletpc/{product_id}",  
    summary="Get products of tabletpc spac by product_id",
    status_code=status.HTTP_200_OK,)
async def check_tabletpc_specificatoin_data(product_id: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await check_tabletpc_specificatoin_data_from_DB(product_id, db)  # 서비스 로직 호출
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
