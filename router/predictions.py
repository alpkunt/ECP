from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay, UserUpdate, UserDisplay2
from db.database import get_db
from db import db_predictions
from typing import List


router = APIRouter(
    prefix= '/predictions',
    tags = ['predictions']
)

@router.post("/days/{date}/{days}")
async def five_days_prediction(date: str, days: int): #,db: Session = Depends(get_db)):
    return db_predictions.days_prediction_and_db(date, days)

@router.post("/hours/{date}/{hours}")
async def twenty_four_hours_prediction(date: str, hours: int): #, db: Session = Depends(get_db)):
    return db_predictions.hours_prediction_and_db(date, hours)
