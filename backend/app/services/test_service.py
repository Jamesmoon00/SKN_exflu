from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.database.models import ProductCategories, Products, Specifications_laptop, Specifications_smartphone, Specifications_tabletpc
from app.schemas.core import PrdCategoryBase, CategoryRequest, ProductRequest, ProductsBase, SpecificationsBase
import base64

async def insert_categories_data_from_DB(specification: SpecificationsBase, db: AsyncSession):
    # 데이터베이스에 새 항목 삽입
    new_specification = Specifications_tabletpc(
        product_id=specification.product_id,
        spec_name=specification.spec_name,
        spec_value=specification.spec_value,
    )
    db.add(new_specification)
    try:
        await db.commit()  # 트랜잭션 커밋
        await db.refresh(new_specification)  # 새로 추가된 항목을 최신 상태로 반환
    except IntegrityError:
        await db.rollback()  # 중복 데이터 등의 문제가 있으면 롤백
        raise HTTPException(status_code=400, detail="Specification already exists")
    
    return new_specification  # 성공적으로 생성된 데이터 반환

async def upload_image(file: UploadFile = File(...)):
    image_data = file.file.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")
    # 파일 정보를 출력
    return encoded_image
    # {
    #     "filename": file.filename,
    #     "content_type": file.content_type,
    #     "size": len(await file.read())
    # }