from pydantic import BaseModel
from typing import Optional
from typing import List


# NOT, display olan herşeyde orm mode True diyeceğiz, çunku, display donerken veri tabanı ile data transformu yaparken problem cıkarmıyor!

class Predictions(BaseModel):
    pass


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Predictions] =[] # yukarda predictions classs olusturduk, aslında liste içinde nested yukardaki predictions listelenecek!
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
    password: Optional[str] = None



