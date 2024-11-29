from pydantic import BaseModel
from typing import Literal, List
from datetime import datetime

class BizContactsDataRequests(BaseModel): # DB 저장
    biz_key :int
    order_date : datetime
    service_name :str
    service_info :str
    budget :int
    period :int
    platform :str
    promo_info :str
    service_target :str
    service_charactors :str
    category_id :int
    
    
class BizContactsDataResponce(BaseModel): # DB 호출
    order_id :int
    biz_key :int
    order_date : datetime
    service_name :str
    service_info :str
    budget :int
    period :int
    platform :str
    promo_info :str
    service_target :str
    service_charactors :str
    category_id :int