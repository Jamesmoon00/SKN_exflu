from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime
from typing import Optional

class BizContactsDataRequests(BaseModel): # DB 저장
    order_date : datetime
    service_name :Optional[str] = None
    service_info :Optional[str] = None
    budget :Optional[str] = None
    period :Optional[str] = None
    platform :Optional[str] = None
    promo_info :Optional[str] = None
    service_target :Optional[str] = None
    service_charactors :Optional[str] = None
    category_id :int
    
    
class BizContactsDataResponse(BaseModel): # DB 호출
    order_id :int
    order_date : datetime
    service_name :Optional[str] = None
    service_info : Optional[str] = None
    budget :Optional[str] = None
    period : Optional[str] = None
    platform :Optional[str] = None
    promo_info : Optional[str] = None
    service_target : Optional[str] = None
    service_charactors :Optional[str] = None
    category_id :int
    UUID : str
    
class BizContactsUpdateModel(BaseModel):
    service_name :Optional[str] = None
    service_info : Optional[str] = None
    budget :Optional[str] = None
    period : Optional[str] = None
    platform :Optional[str] = None
    promo_info : Optional[str] = None
    service_target : Optional[str] = None
    service_charactors :Optional[str] = None