from sqlalchemy.orm import relationship

from db.database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, JSON, ForeignKey

from datetime import datetime, timezone

def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)


class ElectricityConsumption(Base):
    __tablename__ = "elec_cons"
    __table_args__ = {'extend_existing' : True}

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(DateTime(timezone=True))
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    consumption = Column(Float)
    prediction = Column(JSON)
    #prediction_time = Column(DateTime, default=datetime.utcnow().timestamp())
    client_ip = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates='predictions')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key= True)
    created_date = Column(DateTime, default=get_utc_now_timestamp())
    username = Column(String, unique=True)
    email = Column(String)
    hashed_password = Column(String)
    is_Active = Column(Boolean, default=True)
    predictions = relationship('ElectricityConsumption', back_populates='user')
    