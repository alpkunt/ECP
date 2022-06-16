from fastapi import FastAPI, HTTPException
#from fastapi.responses import PlainTextResponse
from router import user, predictions
from db import models
from db.database import engine
from auth import authentication

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(predictions.router)

@app.get("/", tags=['Hello'])
async def root():
    return {"data":"Wellcome to MLOps API"}