from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.models import ProductCategories, Products, Specifications_laptop, Specifications_smartphone, Specifications_tabletpc
from fastapi import HTTPException

async def check_categories_data_from_DB(category_id: int, db: AsyncSession):
    result = await db.execute(
    select(ProductCategories).filter(ProductCategories.category_id == category_id)
    )
    category_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if category_result is None:
        raise HTTPException(status_code=404, detail="There has no product category")
    return category_result


async def check_products_data_from_DB(product_id: int, db: AsyncSession):
    result = await db.execute(
    select(Products).filter(Products.product_id == product_id)
    )
    product_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if product_result is None:
        raise HTTPException(status_code=404, detail="Products are not found")
    return product_result

async def check_laptop_specificatoin_data_from_DB(product_id: int, db: AsyncSession):
    result = await db.execute(
    select(Specifications_laptop).filter(Specifications_laptop.product_id == product_id)
    )
    laptop_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not laptop_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return laptop_result

async def check_smartphone_specificatoin_data_from_DB(product_id: int, db: AsyncSession):
    result = await db.execute(
    select(Specifications_smartphone).filter(Specifications_smartphone.product_id == product_id)
    )
    smartphone_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not smartphone_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return smartphone_result

async def check_tabletpc_specificatoin_data_from_DB(product_id: int, db: AsyncSession):
    result = await db.execute(
    select(Specifications_tabletpc).filter(Specifications_tabletpc.product_id == product_id)
    )
    tabletpc_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not tabletpc_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return tabletpc_result