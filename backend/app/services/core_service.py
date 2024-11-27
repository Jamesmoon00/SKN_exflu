from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database.models import ProductCategories, Products, Specifications_laptop, Specifications_smartphone, Specifications_tabletpc
from app.schemas.core import PrdCategoryBase, CategoryRequest, ProductRequest, ProductsBase, SpecificationsBase

async def search_categories_from_DB(request: CategoryRequest, db: AsyncSession):
    result = await db.execute(
        select(ProductCategories).filter(ProductCategories.category_id == request.category_id)
    )
    category_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if category_result is None:
        return {"message": "No products found"}
    return PrdCategoryBase(category_name= category_result.category_name)


async def search_products_from_DB(request: ProductRequest, db: AsyncSession):
    result = await db.execute(
        select(Products).filter(Products.product_id == request.product_id)
    )
    product_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if product_result is None:
        return {"message": "No products found"}
    return ProductsBase(category_id= product_result.category_id,
                        product_name= product_result.product_name,
                        brand= product_result.brand,
                        model=product_result.model)


async def search_specifications_laptop_from_DB(request: ProductRequest, db: AsyncSession):
    result = await db.execute(
        select(Specifications_laptop).filter(Specifications_laptop.product_id == request.product_id)
    )
    results = result.scalars().all()
    if not results:
        return {"message": "No products found"}
    # 여러 개의 결과를 직렬화하여 반환
    return [
        SpecificationsBase(
            product_id=item.product_id,
            spec_name=item.spec_name,
            spec_value=item.spec_value
        )
        for item in results
    ]


async def search_specifications_smartphone_from_DB(request: ProductRequest, db: AsyncSession):
    result = await db.execute(
        select(Specifications_smartphone).filter(Specifications_smartphone.product_id == request.product_id)
    )
    results = result.scalars().all()
    if not results:
        return {"message": "No products found"}
    # 여러 개의 결과를 직렬화하여 반환
    return [
        SpecificationsBase(
            product_id=item.product_id,
            spec_name=item.spec_name,
            spec_value=item.spec_value
        )
        for item in results
    ]


async def search_specifications_tabletpc_from_DB(request: ProductRequest, db: AsyncSession):
    result = await db.execute(
        select(Specifications_tabletpc).filter(Specifications_tabletpc.product_id == request.product_id)
    )
    results = result.scalars().all()
    if not results:
        return {"message": "No products found"}
    # 여러 개의 결과를 직렬화하여 반환
    return [
        SpecificationsBase(
            product_id=item.product_id,
            spec_name=item.spec_name,
            spec_value=item.spec_value
        )
        for item in results
    ]
