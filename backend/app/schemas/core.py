from pydantic import BaseModel

class ProductRequest(BaseModel): # DB에서 제품 목록 체크
    product_id: int
    
class CategoryRequest(BaseModel): # DB에서 제품 카테고리 체크
    category_id: int

class PrdCategoryBase(BaseModel): #
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