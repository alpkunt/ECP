from pydantic import BaseModel, Field
from typing import Optional
from typing import List, Dict
from datetime import datetime, timezone



def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)

# NOT, display olan herşeyde orm mode True diyeceğiz, çunku, display donerken veri tabanı ile data transformu yaparken problem cıkarmıyor!

class Predictions(BaseModel):
    date: datetime
    prediction: Dict
    class Config:
        orm_mode =True


class UserBase(BaseModel):
    username:str
    email: str
    password: str
    #created_date: Union[datetime, None] = Body(default=None)
    created_date: datetime = Field(get_utc_now_timestamp())
    is_Active: Optional[bool] = True

class UserDisplay(BaseModel):
    username: str
    email: str
    predictions: List[Predictions] =[] # yukarda predictions classs olusturduk, aslında liste içinde nested yukardaki predictions listelenecek!
    # dikkat get all users dendiğinde, itemsta olduğu gibi geliyor!
    # yani kullanıcının ne kadar ürettiği icerik var hepsi geliyor. Bir mantık hatası var burda
    class Config:
        orm_mode = True

class UserDisplay2(BaseModel):
    username: str
    email: str
    items: List[Predictions] = []
    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    #password: Optional[str]

class UserID(UserBase):
    id: int

