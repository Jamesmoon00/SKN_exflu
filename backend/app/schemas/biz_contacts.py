from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime

class BizContactsDataRequests(BaseModel): # DB 저장
    order_date : datetime
    service_name :str
    service_info :str
    budget :str
    period :str
    platform :str
    promo_info :str
    service_target :str
    service_charactors :str
    category_id :int
    
    
class BizContactsDataResponce(BaseModel): # DB 호출
    order_id :int
    order_date : datetime
    service_name :str
    service_info :str
    budget :str
    period :str
    platform :str
    promo_info :str
    service_target :str
    service_charactors :str
    category_id :int