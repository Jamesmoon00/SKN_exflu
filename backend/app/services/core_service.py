from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.future import select
from fastapi import HTTPException
from app.database.models import ProductCategories, Products, Specifications_laptop, Specifications_smartphone, Specifications_tabletpc
from app.schemas.core import PrdCategoryBase, CategoryRequest, ProductRequest, ProductsBase, SpecificationsBase

async def view_all_data_from_DB(db: AsyncSession):
    """
    데이터베이스에서 모든 카테고리, 물건, 스펙 데이터를 검색하여 반환합니다.
    빈 스펙 데이터는 반환하지 않습니다.
    """
    try:
        # 모든 데이터를 로드
        query = await db.execute(
            select(ProductCategories)
            .options(
                selectinload(ProductCategories.products)
                .selectinload(Products.laptop_specs),     # Laptop 스펙
                selectinload(ProductCategories.products)
                .selectinload(Products.smartphone_specs), # Smartphone 스펙
                selectinload(ProductCategories.products)
                .selectinload(Products.tablet_specs),     # Tablet PC 스펙
            )
        )
        categories = query.scalars().all()

        # 데이터 변환
        response_data = [
            {
                "category_id": category.category_id,
                "category_name": category.category_name,
                "products": [
                    {
                        "product_id": product.product_id,
                        "product_name": product.product_name,
                        "brand": product.brand,
                        "model": product.model,
                        **{
                            key: value
                            for key, value in {
                                "laptop_specs": [
                                    {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                    for spec in product.laptop_specs
                                ],
                                "smartphone_specs": [
                                    {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                    for spec in product.smartphone_specs
                                ],
                                "tablet_specs": [
                                    {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                    for spec in product.tablet_specs
                                ],
                            }.items()
                            if value  # 빈 리스트를 제거
                        }
                    }
                    for product in category.products
                ],
            }
            for category in categories
        ]

        # 반환 데이터
        return response_data

    except Exception as e:
        print(f"Error in view_all_data_from_DB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def view_data_by_category_from_DB(category_id: CategoryRequest, db: AsyncSession):
    """
    특정 카테고리의 제품 및 스펙 데이터를 검색하여 반환합니다.
    """
    try:
        # 특정 카테고리 데이터를 로드
        query = await db.execute(
            select(ProductCategories)
            .options(
                selectinload(ProductCategories.products)
                .selectinload(Products.laptop_specs),     # Laptop 스펙
                selectinload(ProductCategories.products)
                .selectinload(Products.smartphone_specs), # Smartphone 스펙
                selectinload(ProductCategories.products)
                .selectinload(Products.tablet_specs),     # Tablet PC 스펙
            )
            .where(ProductCategories.category_id == category_id)  # 카테고리 필터링
        )
        category = query.scalars().first()

        # 카테고리가 존재하지 않을 경우
        if not category:
            raise HTTPException(status_code=404, detail=f"Category with id {category_id} not found.")

        # 데이터 변환
        response_data = {
            "category_id": category.category_id,
            "category_name": category.category_name,
            "products": [
                {
                    "product_id": product.product_id,
                    "product_name": product.product_name,
                    "brand": product.brand,
                    "model": product.model,
                    **{
                        key: value
                        for key, value in {
                            "laptop_specs": [
                                {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                for spec in product.laptop_specs
                            ],
                            "smartphone_specs": [
                                {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                for spec in product.smartphone_specs
                            ],
                            "tablet_specs": [
                                {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                                for spec in product.tablet_specs
                            ],
                        }.items()
                        if value  # 빈 리스트 제거
                    }
                }
                for product in category.products
            ],
        }

        # 반환 데이터
        return response_data

    except Exception as e:
        print(f"Error in view_data_by_category_from_DB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def view_data_by_product_id_from_DB(product_id: int, db: AsyncSession):
    """
    제품 ID를 기반으로 제품과 관련된 스펙 데이터를 검색하여 반환합니다.
    """
    try:
        # 특정 제품 데이터를 로드
        query = await db.execute(
            select(Products)
            .options(
                selectinload(Products.laptop_specs),     # Laptop 스펙
                selectinload(Products.smartphone_specs), # Smartphone 스펙
                selectinload(Products.tablet_specs),     # Tablet PC 스펙
                selectinload(Products.category),         # 카테고리 로드
            )
            .where(Products.product_id == product_id)    # 제품 ID 필터링
        )
        product = query.scalars().first()

        # 제품이 존재하지 않을 경우
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with id {product_id} not found.")

        # 데이터 변환
        response_data = {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "brand": product.brand,
            "model": product.model,
            "category": {
                "category_id": product.category.category_id,
                "category_name": product.category.category_name
            } if product.category else None,
            **{
                key: value
                for key, value in {
                    "laptop_specs": [
                        {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                        for spec in product.laptop_specs
                    ],
                    "smartphone_specs": [
                        {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                        for spec in product.smartphone_specs
                    ],
                    "tablet_specs": [
                        {"spec_name": spec.spec_name, "spec_value": spec.spec_value}
                        for spec in product.tablet_specs
                    ],
                }.items()
                if value  # 빈 리스트 제거
            }
        }

        # 반환 데이터
        return response_data

    except Exception as e:
        print(f"Error in view_data_by_product_id_from_DB: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")



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
