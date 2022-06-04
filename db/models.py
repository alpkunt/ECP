from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy_utils import EmailType
from datetime import datetime


class ElectricityConsumption(Base):
    __tablename__ = "elec_cons"
    __table_args__ = {'extend_existing' : True}

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(DateTime(timezone=True))
    year = Column(DateTime)
    month = Column(DateTime)
    day = Column(DateTime)
    hour = Column(DateTime)
    consumption = Column(Float)
    prediction = Column(Float)
    prediction_time = Column(DateTime, default=datetime.utcnow().timestamp())
    client_ip = Column(String)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key= True)
    created_date = Column(DateTime, default=datetime.utcnow().timestamp())
    username = Column(String, unique=True)
    email = Column(EmailType)
    hashed_password = Column(String)
    is_Active = Column(Boolean, default=True)