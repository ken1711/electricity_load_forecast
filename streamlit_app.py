# streamlit_app.py
import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000") 
Final_Prediction = f"{API_URL}/predict"

# Header Section
st.header("Electricity Load Forecasting Dashboard")

st.markdown(
    """
    This dashboard demonstrates an end-to-end machine learning workflow:

    - A FastAPI backend serving a trained ML model  
    - A Streamlit frontend for real-time predictions  
    - Fully containerized using Docker and Docker Compose  
    - Ready for deployment to Cloud environments
    - Designed as a portfolio project for recruiters and hiring managers

    Use the sidebar to enter feature values and click **Predict load** to generate a forecast.
    """
)

# API Documentation
st.subheader("API Documentation")
st.markdown(
    f"""
    **Open Swagger UI**
    [View API Documentation]({API_URL}/docs)
    """
)
# Backend URL 
st.subheader("Backend API Endpoint")
st.markdown(f"Connected: {API_URL}")

# Sidebar Inputs
st.sidebar.header("Input Features")

st.sidebar.subheader("Time Features")
Hour_of_day = st.sidebar.number_input("Hour of day (0-23)", 0, 23, 12)
Day_of_week = st.sidebar.number_input("Day of week (0=Mon, 6=Sun)", 0, 6, 2)
Is_weekend = st.sidebar.selectbox("Is weekend?", (0, 1))
Quarter_of_year = st.sidebar.number_input("Quarter of year (1-4)", 1, 4, 1)
Month = st.sidebar.number_input("Month (1-12)", 1, 12, 1)
Year = st.sidebar.number_input("Year", 2000, 2100, 2024)
Day_of_year = st.sidebar.number_input("Day of year (1-366)", 1, 366, 100)

st.sidebar.subheader("Historical Load (MW)")
Load_1_hour_ago = st.sidebar.number_input("Load 1 hour ago (MW)", value=30000.0)
Load_24_hours_ago = st.sidebar.number_input("Load 24 hours ago (MW)", value=29000.0)
Load_48_hours_ago = st.sidebar.number_input("Load 48 hours ago (MW)", value=28000.0)
Load_1_week_ago = st.sidebar.number_input("Load 1 week ago (MW)", value=27000.0)
Load_30_days_ago = st.sidebar.number_input("Load 30 days ago (MW)", value=26000.0)

st.sidebar.subheader("Rolling Statistics (MW)")
Average_load_over_last_24_hours = st.sidebar.number_input("Average load over last 24 hours (MW)", value=29500.0)
Variation_in_load_over_last_24_hours = st.sidebar.number_input("Variation in load over last 24 hours (std dev)", value=500.0)
Average_load_over_last_week = st.sidebar.number_input("Average load over last week (MW)", value=28000.0)

# Prediction Section
st.subheader("Generate Load Prediction")

if st.button("Predict load"):
    payload = {
        "Hour_of_day": Hour_of_day,
        "Day_of_week": Day_of_week,
        "Is_weekend": Is_weekend,
        "Quarter_of_year": Quarter_of_year,
        "Month": Month,
        "Year": Year,
        "Day_of_year": Day_of_year,
        "Load_1_hour_ago": Load_1_hour_ago,
        "Load_24_hours_ago": Load_24_hours_ago,
        "Load_48_hours_ago": Load_48_hours_ago,
        "Load_1_week_ago": Load_1_week_ago,
        "Load_30_days_ago": Load_30_days_ago,
        "Average_load_over_last_24_hours": Average_load_over_last_24_hours,
        "Variation_in_load_over_last_24_hours": Variation_in_load_over_last_24_hours,
        "Average_load_over_last_week": Average_load_over_last_week,
    }

    try:
        response = requests.post(Final_Prediction, json = payload, timeout = 10)
        if response.status_code == 200:
            result = response.json()
            st.subheader("Prediction result")
            st.write(f"Model: {result['model']}")
            st.success(f"Predicted load: {result['predicted_load']:.2f} {result['unit']}")
            st.json(result["business_input"])
        else:
            st.error(f"API error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")