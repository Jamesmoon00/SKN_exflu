from typing import Union
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
from app import models
from sqlalchemy.future import select
from app.database import engine, AsyncSessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, Depends
from fastapi_health import health
import uvicorn

#####################

"""Entrypoint to invoke the FastAPI application service with."""



app = FastAPI()


class HealthCheck(BaseModel):
    """Response model to validate and return when performing a health check."""

    status: str = "OK"

@app.get("/")
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
        yield session

@app.get("/ProductCategories/{category_id}", status_code=status.HTTP_200_OK)
async def read_user(category_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.ProductCategories).filter(models.ProductCategories.category_id == category_id)
    )
    category_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if category_result is None:
        raise HTTPException(status_code=404, detail="There has no product category")
    return category_result

@app.get("/Products/{product_id}", status_code=status.HTTP_200_OK)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Products).filter(models.Products.product_id == product_id)
    )
    product_result = result.scalar_one_or_none()  # 첫 번째 결과 반환 또는 None
    if product_result is None:
        raise HTTPException(status_code=404, detail="Products are not found")
    return product_result

@app.get("/Specifications_laptop/{product_id}", status_code=status.HTTP_200_OK)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Specifications_laptop).filter(models.Specifications_laptop.product_id == product_id)
    )
    laptop_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not laptop_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return laptop_result

@app.get("/Specifications_smartphone/{product_id}", status_code=status.HTTP_200_OK)
async def read_user(product_id: int, db: Session = Depends(get_db)):
    result = await db.execute(
    select(models.Specifications_smartphone).filter(models.Specifications_smartphone.product_id == product_id)
    )
    smartphone_result = result.scalars().all()  # 첫 번째 결과 반환 또는 None
    if not smartphone_result:
        raise HTTPException(status_code=404, detail="Products are not found")
    return smartphone_result

@app.get("/Specifications_tabletpc/{product_id}", status_code=status.HTTP_200_OK)
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