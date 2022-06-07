import joblib
from datetime import datetime

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
    print("degerler: ", result)

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
    print("degerler: ", result)

    return result

######################################

def days_prediction_and_db(date,days):
     result = predictions_by_date_day(forecaster, date, days)
     """db db db db"""
     return result

def hours_prediction_and_db(date, hours):
    result = predictions_by_date_hour(forecaster, date, hours)
    """db db db"""
    return result