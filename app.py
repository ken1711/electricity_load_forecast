from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd 

class loadFeatureInput(BaseModel):
    Hour_of_day: int
    Day_of_week: int
    Is_weekend: int
    Quarter_of_year: int
    Month: int
    Year: int
    Day_of_year: int
    Load_1_hour_ago: float
    Load_24_hours_ago: float
    Load_48_hours_ago: float
    Load_1_week_ago: float
    Load_30_days_ago: float 
    Average_load_over_last_24_hours: float 
    Variation_in_load_over_last_24_hours: float 
    Average_load_over_last_week: float 

BusinessFeatures_To_InternalFeatures = {
    "Hour_of_day": "hour",
    "Day_of_week": "dayofweek",
    "Is_weekend": "is_weekend",
    "Quarter_of_year": "quarter",
    "Month": "month",
    "Year": "year",
    "Day_of_year": "dayofyear",
    "Load_1_hour_ago": "electricity_load_lag_1",
    "Load_24_hours_ago": "electricity_load_lag_24",
    "Load_48_hours_ago": "electricity_load_lag_48",
    "Load_1_week_ago": "electricity_load_lag_168",
    "Load_30_days_ago": "electricity_load_lag_720",
    "Average_load_over_last_24_hours": "electricity_load_rolling_24_mean",
    "Variation_in_load_over_last_24_hours": "electricity_load_rolling_std_24",
    "Average_load_over_last_week": "electricity_load_rolling_mean_168",
}

Feature_Model_Order = [
    "hour",
    "dayofweek",
    "is_weekend",
    "quarter",
    "month",
    "year",
    "dayofyear",
    "electricity_load_lag_1",
    "electricity_load_lag_24",
    "electricity_load_lag_48",
    "electricity_load_lag_168",
    "electricity_load_lag_720",
    "electricity_load_rolling_24_mean",
    "electricity_load_rolling_std_24",
    "electricity_load_rolling_mean_168",
] 

app = FastAPI(
    title = "Electricity Load Forecast API",
    description = "Forecast electricity load using an XGBoost ML Model",
    version = "1.0"
)

model = joblib.load("electricity_xgb_model.joblib")

def build_model_input_data(business_input: dict):
    internal_dict = {
        BusinessFeatures_To_InternalFeatures[key]: value
        for key, value in business_input.items()
    }
    
    data = pd.DataFrame([[internal_dict[col] for col in Feature_Model_Order]],
                        columns = Feature_Model_Order
    )
    return data, internal_dict

@app.get("/", summary = "Health check")
def home():
    return {"message": "Electricity Load Forecasting API is running"}


@app.post("/predict", summary = "Predict electricity load")
def predict_model1(input_features: loadFeatureInput):
    business_input = input_features.model_dump()
    data, internal_dict = build_model_input_data(business_input)
    prediction = model.predict(data)[0]

    return {
        "model": "XGBoost",
        "business_input": business_input,
        "internal_model_input": internal_dict,
        "predicted_load": round(float(prediction), 2),
        "unit": "MegaWatts (MW)"
    }