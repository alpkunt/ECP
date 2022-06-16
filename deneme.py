import json
from datetime import datetime, timezone
from sqlalchemy.sql import func
from db import models
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.requests import Request

load_dotenv()  # take environment variables from .env.
SQLALCHEMY_DATABASE_URL=os.getenv('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
#print(func.now())


#print(datetime.utcnow().timestamp())


def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)

#print("Alper :",get_utc_now_timestamp())

print(datetime.now())

print(datetime.now().year)

print(type(datetime.now().year))

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

def insert_prediction(prediction_result, client_ip, db):
    date = datetime.now()

    new_prediction_result = models.ElectricityConsumption(
        date=date,
        year=date.year,
        month=date.month,
        day=date.day,
        hour=date.hour,
        consumption=None,  # burası, gerçek değer ölçüldükten sonra update edileceği için başlangıçta null verdim.
        prediction=prediction_result,  # burada mecburen kolona bir liste veya bir dictionary falan göndereceğiz!
        client_ip=client_ip
    )
    db.add(new_prediction_result)
    db.commit()
    db.refresh(new_prediction_result)
    return new_prediction_result

def client_data(request: Request):
    client_host = request.client.host
    client_port = request.client.port

    return {"client_host": client_host, "client_port": client_port}



#client_ip = client_data()
#prediction_result = {"alper" : "malper", "hayta" : "zort"}
#prediction_result = {"asdasd": "alper alper", "asd": 213}
#prediction_result =  {"1654300800000":34655.8040793578,"1654304400000":33993.8550418576,"1654308000000":33450.3507887045,"1654311600000":33060.7152944858,"1654315200000":32852.6109953291,"1654318800000":32886.4714382248,"1654322400000":33228.9704376123}





def prediction1(forecaster,date: str,days: int):

    import numpy as np
    import pandas as pd
    # Modelling and Forecasting
    # ==============================================================================
    from sklearn.linear_model import Ridge
    #from lightgbm import LGBMRegressor
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_absolute_error
    from skforecast.ForecasterAutoreg import ForecasterAutoreg
    from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
    from skforecast.model_selection import grid_search_forecaster
    from skforecast.model_selection import backtesting_forecaster
    from datetime import timedelta

    start_date = datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
    print(forecaster)
    steps = 500
    print("Days :", days)
    print("Horizon:", steps )
    print("degerler: ",forecaster.predict(steps).loc[start_date:start_date+timedelta(days=5)])

    return forecaster.predict(steps).loc[start_date:]


def predictions_by_date_hour(forecaster, date: str, hours: int):
    import numpy as np
    import pandas as pd
    # Modelling and Forecasting
    # ==============================================================================
    from sklearn.linear_model import Ridge
    # from lightgbm import LGBMRegressor
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_absolute_error
    from skforecast.ForecasterAutoreg import ForecasterAutoreg
    from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
    from skforecast.model_selection import grid_search_forecaster
    from skforecast.model_selection import backtesting_forecaster
    from datetime import timedelta

    start_date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    print(forecaster)
    steps = 500
    print("Hours :", hours)
    print("Horizon:", steps)
    result = forecaster.predict(steps).loc[start_date:start_date + timedelta(hours=hours)]
    #print("degerler: ", result)

    return result


def prediction(forecaster, days: int):

    import numpy as np
    import pandas as pd
    # Modelling and Forecasting
    # ==============================================================================
    from sklearn.linear_model import Ridge
    #from lightgbm import LGBMRegressor
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import mean_absolute_error
    from skforecast.ForecasterAutoreg import ForecasterAutoreg
    from skforecast.ForecasterAutoregMultiOutput import ForecasterAutoregMultiOutput
    from skforecast.model_selection import grid_search_forecaster
    from skforecast.model_selection import backtesting_forecaster



    print(forecaster)
    steps = days * 24
    print("Days :", days)
    print("Horizon:", steps )
    print(forecaster.predict(steps))
import joblib

forecaster = joblib.load("pred_models/forecaster.pkl")
date = "2022-06-04 00:00:00"
#prediction1(forecaster, date, 5)

prediction_result = predictions_by_date_hour(forecaster, date, 6)

prediction_result_json = prediction_result.to_json(date_format='iso', double_precision=2)
print("pred :", prediction_result_json)

prediction_result_json_parsed = json.loads(prediction_result_json)

print("Parsed :", prediction_result_json_parsed)


client_ip = "123.465.78.45"

#prediction_result = {"1654300800000":34655.8040793578,"1654304400000":33993.8550418576,"1654308000000":33450.3507887045,"1654311600000":33060.7152944858,"1654315200000":32852.6109953291,"1654318800000":32886.4714382248,"1654322400000":33228.9704376123}

insert_prediction(prediction_result_json_parsed, client_ip, db)

# BUnu dene mutlaka --- >> modele json yerine jsonb yapmak : from sqlalchemy.dialects.postgresql import JSONB