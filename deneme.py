from datetime import datetime, timezone
from sqlalchemy.sql import func

print(func.now())


print(datetime.utcnow().timestamp())


def get_utc_now_timestamp() -> datetime:
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)

#print("Alper :",get_utc_now_timestamp())

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
    print("degerler: ", result)

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

predictions_by_date_hour(forecaster, date, 6)
