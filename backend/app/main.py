from typing import List, Optional, Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from app import models
from sqlalchemy.future import select
from app.database.database import engine, AsyncSessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Depends
from fastapi_health import health
import uvicorn

#####################

"""Entrypoint to invoke the FastAPI application service with."""



app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://streamlitllmcore.jamesmoon.click"],  # 모든 도메인 허용
    allow_methods=["*"],  # 모든 HTTP 메서드 허용 (GET, POST, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"

@app.get(
    "/",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def root():
    return {"status": "OK"}

@app.get(
    "/health",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
def get_health() -> HealthCheck:
    """
    ## Perform a Health Check
    Endpoint to perform a healthcheck on. This endpoint can primarily be used Docker
    to ensure a robust container orchestration and management is in place. Other
    services which rely on proper functioning of the API service will not deploy if this
    endpoint returns any other HTTP status code except 200 (OK).
    Returns:
        HealthCheck: Returns a JSON response with the health status
    """
    return HealthCheck(status="OK")


def main() -> None:
    """Entrypoint to invoke when this module is invoked on the remote server."""
    # See the official documentations on how "0.0.0.0" makes the service available on
    # the local network - https://www.uvicorn.org/settings/#socket-binding
    uvicorn.run("main:app", host="0.0.0.0")


if __name__ == "__main__":
    main()

"""
To check if the API service works as expected, perform the following actions:
    1. Run the API service by invoking this command - "python -m main".
    2. If the service is running, open the URL "http://localhost:8000" in your browser.
    3. With cURL, invoke this command:
       "curl --include --request GET "http://localhost:8000/health" and you should
       get a HTTP Status Code 200 OK message somewhere in it."
An example Dockerfile with a healthcheck capabilities enabled is available in this gist:
https://gist.github.com/Jarmos-san/11bf22c59d26daf0aa5223bdd50440da
"""

#####################

class ProductRequest(BaseModel):
    product_id: int
    
class CategoryRequest(BaseModel):
    category_id: int

# FastAPI 애플리케이션을 초기화합니다.
# app = FastAPI()
# 데이터베이스 모델을 생성합니다.
# models.Base.metadata.create_all(bind=engine)

# class로 다룰 때, primary_key를 다루지 않음
# 외래키는 다루긴 함
# product categories 모델의 기본 구조를 정의합니다.
class PrdCategoryBase(BaseModel):
    category_name:str

# Products 모델의 기본 구조를 정의합니다.
class ProductsBase(BaseModel):
    category_id:int
    product_name:str
    brand:str
    model:str

# SpecificationsBase 모델의 기본 구조를 정의합니다.
class SpecificationsBase(BaseModel):
    product_id:int
    spec_name:str
    spec_value:str

# 세션 생성 함수
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()  # 세션이 반드시 닫히도록 설정

        
@app.post("/productcategories", 
    tags=["Database"],
    summary="Get product categories",
    status_code=status.HTTP_200_OK,)
async def read_user(request: CategoryRequest,db: Session = Depends(get_db)):
    result = await db.execute(
        select(models.ProductCategories).filter(models.ProductCategories.category_id == request.category_id)
    )
    category_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if category_result is None:
        return {"message": "No products found"}
    return PrdCategoryBase(category_name= category_result.category_name)

@app.post("/products", 
    tags=["Database"],
    summary="Get products",
    status_code=status.HTTP_200_OK,)
async def read_user(request: ProductRequest, db: Session = Depends(get_db)):
    result = await db.execute(
        select(models.Products).filter(models.Products.product_id == request.product_id)
    )
    product_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if product_result is None:
        return {"message": "No products found"}
    return ProductsBase(category_id= product_result.category_id,
                        product_name= product_result.product_name,
                        brand= product_result.brand,
                        model=product_result.model)
###
@app.post("/specifications_laptop", 
    tags=["Database"],
    summary="Get products of laptop spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def read_user(request: ProductRequest, db: Session = Depends(get_db)):
    result = await db.execute(
        select(models.Specifications_laptop).filter(models.Specifications_laptop.product_id == request.product_id)
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

@app.post("/specifications_smartphone", 
    tags=["Database"],
    summary="Get products of smartphone spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def read_user(request: ProductRequest, db: Session = Depends(get_db)):
    result = await db.execute(
        select(models.Specifications_smartphone).filter(models.Specifications_smartphone.product_id == request.product_id)
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
@app.post("/specifications_tabletpc", 
    tags=["Database"],
    summary="Get products of tabletpc spac",
    status_code=status.HTTP_200_OK,
    response_model=List[SpecificationsBase],  # 여러 항목 반환을 명시
)
async def read_user(request: ProductRequest, db: Session = Depends(get_db)):
    result = await db.execute(
        select(models.Specifications_tabletpc).filter(models.Specifications_tabletpc.product_id == request.product_id)
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

@app.post("/productcategories/{category_id}", 
    tags=["Check Database"],
    summary="Get product categories",
    status_code=status.HTTP_200_OK,)
async def read_user(category_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.ProductCategories).filter(models.ProductCategories.category_id == category_id)
    )
    category_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if category_result is None:
        raise HTTPException(status_code=404, detail="There has no product category")
    return category_result

@app.post("/products/{product_id}", 
    tags=["Check Database"],
    summary="Get products info by product_id",
    status_code=status.HTTP_200_OK,)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Products).filter(models.Products.product_id == product_id)
    )
    product_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if product_result is None:
        raise HTTPException(status_code=404, detail="Products are not found")
    return product_result

@app.post("/specifications_laptop/{product_id}", 
    tags=["Check Database"],
    summary="Get products of laptop spac by product_id",
    status_code=status.HTTP_200_OK,)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Specifications_laptop).filter(models.Specifications_laptop.product_id == product_id)
    )
    laptop_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not laptop_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return laptop_result

@app.post("/specifications_smartphone/{product_id}",  
    tags=["Check Database"],
    summary="Get products of smartphone spac by product_id",
    status_code=status.HTTP_200_OK,)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Specifications_smartphone).filter(models.Specifications_smartphone.product_id == product_id)
    )
    smartphone_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not smartphone_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return smartphone_result

@app.post("/specifications_tabletpc/{product_id}",  
    tags=["Check Database"],
    summary="Get products of tabletpc spac by product_id",
    status_code=status.HTTP_200_OK,)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Specifications_tabletpc).filter(models.Specifications_tabletpc.product_id == product_id)
    )
    tabletpc_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not tabletpc_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return tabletpc_result

# @app.post("/Specifications_tabletpc/", status_code=status.HTTP_201_CREATED)
# async def create_tabletpc_specification(specification: SpecificationsBase, db: AsyncSession = Depends(get_db), ):
#     # 데이터베이스에 새 항목 삽입
#     new_specification = models.Specifications_tabletpc(
#         product_id=specification.product_id,
#         spec_name=specification.spec_name,
#         spec_value=specification.spec_value,
#     )
#     db.add(new_specification)
#     try:
#         await db.commit()  # 트랜잭션 커밋
#         await db.refresh(new_specification)  # 새로 추가된 항목을 최신 상태로 반환
#     except IntegrityError:
#         await db.rollback()  # 중복 데이터 등의 문제가 있으면 롤백
#         raise HTTPException(status_code=400, detail="Specification already exists")
    
#     return new_specification  # 성공적으로 생성된 데이터 반환

# 요청 데이터 모델 정의
class Item(BaseModel):
    name: str
    value: int

# POST 엔드포인트 정의
@app.post("/process/",  
    tags=["Check server connection"],
    summary="Get products of tabletpc spac by product_id",
    status_code=status.HTTP_200_OK,)
async def process_item(item: Item):
    # 클라이언트에서 받은 데이터를 처리 후 반환
    return {"message": f"Received {item.name} with value {item.value}"}
