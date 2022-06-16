from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from schemas import UserBase
from db.database import get_db
from db import db_predictions

from auth.oauth2 import get_current_user

router = APIRouter(
    prefix='/predictions',
    tags=['predictions']
)

@router.post("/days/{date}/{days}")
async def five_days_prediction(date: str, days: int, request: Request ,db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data' :  db_predictions.days_prediction_and_db(date, days, request, db, current_user),
            'current_user' : current_user.username,
            'current_user_email' : current_user.email
    }

@router.post("/hours/{date}/{hours}")
async def twenty_four_hours_prediction(date: str, hours: int,request: Request, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return {
        'data' : db_predictions.hours_prediction_and_db(date, hours, request, db, current_user),
        'current_user' : current_user.username,
        'current_user_email' : current_user.email
    }

