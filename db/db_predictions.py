import json
import joblib
from datetime import datetime
from db import models

forecaster = joblib.load("pred_models/forecaster.pkl")

def predictions_by_date_day(forecaster, date: str,days: int):

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
    result = forecaster.predict(steps).loc[start_date:start_date+timedelta(days=days)]
    #print("degerler: ", result)

    return result


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
    result = forecaster.predict(steps).loc[start_date:start_date + timedelta(hours=hours-1)]
    #print("degerler: ", result)

    return result

######################################

def insert_prediction(prediction_result, request, db, current_user):
    date = datetime.now()

    new_prediction_result = models.ElectricityConsumption(
        date = date,
        year = date.year,
        month = date.month,
        day= date.day,
        hour = date.hour,
        consumption= None, # burası, gerçek değer ölçüldükten sonra update edileceği için başlangıçta null verdim.
        prediction= prediction_result, #burada mecburen kolona bir liste veya bir dictionary falan göndereceğiz!
        client_ip= request.client.host,
        user_id=current_user.id
    )


    db.add(new_prediction_result)
    db.commit()
    db.refresh(new_prediction_result)
    return new_prediction_result




def days_prediction_and_db(date,days, request, db, current_user):
    prediction_result = predictions_by_date_day(forecaster, date, days)
    prediction_result_json = prediction_result.to_json(date_format='iso', double_precision=2)
    prediction_result_json_parsed = json.loads(prediction_result_json)
    """db db db db"""
    insert_prediction(prediction_result_json_parsed,request, db,current_user)
    # return prediction_result olarak gönderince pandas series object yolluyor responsea
    return prediction_result_json_parsed

def hours_prediction_and_db(date, hours,request,db, current_user):
    prediction_result = predictions_by_date_hour(forecaster, date, hours)
    prediction_result_json = prediction_result.to_json(date_format='iso', double_precision=2)
    prediction_result_json_parsed = json.loads(prediction_result_json)

    """db db db"""
    insert_prediction(prediction_result_json_parsed, request, db, current_user)
    return prediction_result_json_parsed