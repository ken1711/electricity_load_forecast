# ⚡Electricity Load Forecasting

![Python](https://img.shields.io/badge/Python-3.13-blue) ![XGBoost](https://img.shields.io/badge/XGBoost-Model-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green) ![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)![Docker](https://img.shields.io/badge/Docker-Containerized-blue) ![Azure](https://img.shields.io/badge/Azure-Container_Apps-lightblue)

Machine learning–based forecasting of hourly electricity load in Germany using ENTSO-E data, delivered through a FastAPI backend and Streamlit frontend, and fully containerized for deployment on Azure Container Apps.


## 📌Project Overview

Electricity load forecasting is critical for maintaining a stable and efficient power system. Because electricity cannot be stored at scale, supply must continuously match demand. Accurate predictions enable better planning, reduce operational risk, and help prevent disruptions.

This project develops an end-to-end, production-ready machine learning system to forecast hourly electricity demand in Germany.
The model is trained on historical ENTSO-E data, originally recorded at 15-minute intervals and resampled to hourly resolution for time series forecasting.
The solution spans the full lifecycle from data processing and model training to deployment and user interaction.


## 🔗 System Components

| Features       | Description|
| :--------------| :----------|
| Data Pipeline          | Collects and processes historical ENTSO‑E load data| 
|                        | Resamples 15‑minute data to hourly resolution|
|                        | Performs feature engineering for time‑series forecasting|
| Machine Learning Model | XGBoost regression model trained on historical load data|
|                        | Uses engineered time-series features to improve accuracy| 
| Backend (FastAPI)      | Provides a high-performance REST API for real-time predictions| 
|                        | Designed for scalability and low-latency responses|       
| Frontend (Streamlit)   | Offers an interactive interface for user input| 
|                        | Visualization of forecasts|
|                        | Exploration of model outputs| 
| Containerization       | Fully Dockerized architecture ensuring Portability| 
|                        | Reproducibility|
|                        | Consistent deployment across environments|
| Cloud Deployment       | Hosted on Azure Container Apps|
|                        | Supports scale-to-zero, enabling cost-efficient, serverless-style operation|


## 🏗️System Architecture

```bash
       [Historical Load + Timestamps] --> [Feature Engineering]

                                       |
                                       v
                             [XGBoost Model Training]
                                       |
                                       v
                               [Saved via Joblib]
                                       |
                                       v
                             [FastAPI Backend API]
                                       |
                             [Streamlit Frontend]  
                                       |
                                       v
        ┌──────────────────────────────┬──────────────────────────────┐
        │                              │                              │
        ▼                              ▼                              ▼
┌────────────────┐           ┌────────────────┐            ┌────────────────┐
│   FastAPI API  │◄────────► │ Azure Container│◄──────────►│ Streamlit UI   │
│ (Predictions)  │           │     Apps       │            │ (User Facing)  │
└────────────────┘           └────────────────┘            └────────────────┘

```


## 🗂️Project Structure

```bash
electricity-load-forecasting/
│
│
├── data/
│   └── de_data/
│
├── notebooks/
│   ├── 01_eda_electricity_load.ipynb
│   ├── 02_feature_engineering_electricity_load.ipynb
│   ├── 03_modelTraining_evaluationResult_electricity_load.ipynb
│   ├── full_workflow_electricity_load.ipynb
│   └── forecast_electricity_load.html
│
├── models/
│   └── model.joblib
│
├── plots/
│   ├── actual_prediction.png
│   ├── electricityload_hours.png
│   ├── electricityload_month.png
│   ├── electricityload_time.png
│   ├── electricityload_time_1week.png
│   ├── featureimportance.png
│   ├── lags_1weeks.png
│   └── timeseriescrossvalidation.png
│
├── api/
│   ├── Dockerfile.api.py
│   ├── app.py
│   ├── requirements.txt
│   ├── fastapi.png
│   ├── fastapi_docs.demo.gif
│   ├── fastapi_docs.png
│   ├── fastapi_requests.png
│   └── fastapi_responses.png
│
├── streamlit/
│   ├── Dockerfile.streamlit.py
│   ├── streamlit_app.py
│   ├── requirements.streamlit.txt
│   ├── streamlit.png
│   ├── streamlit_UI.demo.gif
│   ├── streamlit_UI_1.png
│   └── streamlit_UI_2.png
│
├── docker-compose.yml
└── README.md
```

## 📊Dataset

The dataset used in this project is publicly available: Mendeley Data - Electricity Load Dataset from 2015 - 2025 

https://data.mendeley.com/datasets/ybggkc58fz/1

[Download direct dataset](https://github.com/ken1711/electricity_load_forecast/tree/main/de_data)

Dataset Notes

- Original resolution: 15 minutes, resampled to hourly frequency
- Contains electricity load data for multiple countries (analysis focused on Germany)
- Designed for time series forecasting and feature engineering, with the creation of time-based and statistical features to improve model performance.

Features Used

- Hourly electricity load values
- Calendar-based features (hour of day, day of week, is weekend, quarter, month, year, day of year)
- Rolling statistics (Mean and Standard deviation)
- Lag features (e.g., 1 hour, 24 hours, 48 hours, 168 hours, 720 hours)


## 🧠Modeling Approach

The modeling pipeline includes:

- Time Series Cross Validation split  
- Feature engineering (date-time, Lag features, Rolling window statistics)  
- Model selection (XGBRegressor)  
- Time-series cross‑validation  
- Error analysis  

[Download Model.joblib](https://github.com/ken1711/electricity_load_forecast/blob/main/model.joblib)

- Results

| Metric | Value     |
| :------| :---------|
| RMSE   | 714.13 MW | 
| MAE    | 536.59 MW |                            
| MAPE   | 1.02 %    |                            
| R2     | 0.99      | 


## 🔗Jupyter Notebooks

All data science work is documented in the notebooks listed below.

- **01 – Exploratory Data Analysis**

![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/electricityload_time.png)
![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/electricityload_time_1week.png)

[Open Notebook](https://github.com/ken1711/electricity_load_forecast/blob/main/notebook/01_eda_electricity_load.ipynb)

- **02 – Feature Engineering** 

![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/electricityload_hours.png)
![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/electricityload_month.png)
![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/lags_1weeks.png)

[Open Notebook](https://github.com/ken1711/electricity_load_forecast/blob/main/notebook/02_feature_engineering_electricity_load.ipynb)

- **03 – Model Training / Evaluation & Results**  

![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/timeseriescrossvalidation.png)

[Open Notebook](https://github.com/ken1711/electricity_load_forecast/blob/main/notebook/03_modelTraining_evaluationResult_electricity_load.ipynb)

- **Full Workflow**  

[Open Notebook](https://github.com/ken1711/electricity_load_forecast/blob/main/notebook/full_workflow_electricity_load.ipynb)

These notebooks demonstrate the full workflow from raw data to final model.

Visualizations include:
 
Feature importance: Available in the evaluation (full workflow) notebook.

![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/featureimportance.png)


Actual vs Predicted: Viewable by downloading and opening the HTML file.

![Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/plots/actual_prediction.png)

Both are included in the evaluation notebook.


## 🚀How to Install and Run the project 

1. Clone repository

git clone https://github.com/ken1711/electricity_load_forecast.git

cd electricity_load_forecast

2. Install all dependencies

pip install -r requirements.txt

3. Run FastAPI

uvicorn app:app --reload

4. Run Streamlit

streamlit run streamlit_app.py


## 🧩FastAPI (Backend)

Code Example

Endpoint

POST /predict  Predict electricity load

This endpoint forecasts electricity load using engineered time-series features such as lag values and rolling statistics.

Request body
curl -X POST "http://localhost:8000/predict" \
-H "Content-Type: application/json" \
-d '{

  "Hour_of_day": 14,

  "Day_of_week": 2,

  "Is_weekend": 0,

  "Quarter_of_year": 2,

  "Month": 5,

  "Year": 2024,

  "Day_of_year": 135,

  "Load_1_hour_ago": 42000.5,

  "Load_24_hours_ago": 41000.2,

  "Load_48_hours_ago": 40500.8,

  "Load_1_week_ago": 39800.3,

  "Load_30_days_ago": 39000.1,

  "Average_load_over_last_24_hours": 41500.6,

  "Variation_in_load_over_last_24_hours": 1200.4,

  "Average_load_over_last_week": 40050.7
}'

Responses
{

  "predicted_load": 42350.78,

  "unit": "MegaWatts (MW)"

}

Interactive API Docs

FastAP: http://localhost:8000/docs

### Prediction
![FastAPI docs Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/api/fastapi_docs.png)

![FastAPI Live Demo](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/api/fastapi_docs.demo.gif)


## 🖥️Streamlit UI
The Streamlit app provides an interactive interface for entering input features and visualizing predictions.

Streamlit: http://localhost:8501

Preview
### Dashboard Home

![Streamlit Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/streamlit/streamlit_UI_1.png)

![Streamlit Live Demo](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/streamlit/streamlit_UI.demo.gif)


## 🐳 Docker and Containerization

### Docker Compose 

Docker Compose is a tool that simplifies running applications made up of multiple containers (like a frontend and backend) using a single configuration file. Instead of starting each container manually, Docker Compose lets you define all services, networks, and volumes in one YAML file and launch the entire application stack with a single command.

services:

  fastapi:

    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: fastapi_service
    ports:
      - "8000:8000"

  streamlit:

    build:
      context: .
      dockerfile: Dockerfile.streamlit
    container_name: streamlit_service
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://fastapi:8000
    depends_on:
      - fastapi

To build and start all services, run:

docker-compose up --build

Once running, open your browser:

FastAPI (Frontend): http://localhost:8501

Streamlit (Backend API): http://localhost:8000


To learn how to build, tag, and publish a Docker image to Docker Hub, follow this guide:

https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/

Docker Hub repositories:

Backend (FastAPI): kenwhite17/backend_fastapi-app:latest

Frontend (Streamlit): kenwhite17/frontend_streamlit-app:latest


## ☁️Deployment (Azure Container Apps)

Azure Container Apps is a serverless platform that simplifies running containerized applications while reducing infrastructure overhead and costs. It eliminates the need to manage server configuration, container orchestration, or deployment processes, providing fully managed and up-to-date resources to keep your applications secure, reliable, and scalable.

For more details about Azure Container Apps, please refer to the links below.

https://learn.microsoft.com/en-us/azure/container-apps/overview

https://learn.microsoft.com/en-us/azure/container-apps/compare-options?source=recommendations

https://learn.microsoft.com/en-us/azure/container-apps/

🔹 Step 1 — Open Container Apps

Go to 👉 https://portal.azure.com
Login
Start by navigating to “Container Apps”

and Click ➕ Create

🔹 Step 2 — Basics tab

Fill this:

Subscription: Azure Subscription 1

Resource Group → Create new: mydatascience_ml_portfolio

Container app name: fastapi-app

Deployment source: Container image

Region: Germany West Europe

Container Apps environment: ml-env (mydatascience_ml_portfolio)

Next

🔹 Step 3 — Container tab

Container details

Name: fastapi-app

Image source → Select: Docker Hub or other registeries

Image type: Public

Registry login server: docker.io

Image and tag: kenwhite17/backend_fastapi-app:latest

Workload profile: Consumption - up to 4 vCPUs, 8 Gib memory

CPU and memory: 0.5 CPU cores, 1 Gi memory

Next

🔹 Step 4 — Ingress (VERY IMPORTANT)

Scroll down to Ingress settings:

Enable ingress: Checked

Ingress traffic: Accepting traffic from Anywhere

Target port: 8000

Click: Review + Create

Wait until the creation is validated (passed), then click Create.
Once the process is complete, navigate to the newly created resource and check its URL. Copy this URL, as it will be needed for the frontend setup.
To confirm the container is running correctly, open the URL and verify that the expected message is displayed.


![FastAPI Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/api/fastapi.png)

[FastAPI Backend Cloud URL:](https://fastapi-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io)


Now deploy Streamlit (the same process)

🔹 Step 1 — Create another Container App

Click Create again

🔹 Step 2 — Basics tab

Fill this:

Subscription: Azure Subscription 1

Resource Group → Create new: mydatascience_ml_portfolio

Container app name: streamlit-app

Deployment source: Container image

Region: Germany West Europe

Container Apps environment: ml-env (mydatascience_ml_portfolio)

Next

🔹 Step 3 — Container tab

Container details

Name: streamlit-app

Image source → Select: Docker Hub or other registeries

Image type: Public

Registry login server: docker.io

Image and tag: kenwhite17/backend_fastapi-app:latest

Workload profile: Consumption - up to 4 vCPUs, 8 Gib memory

CPU and memory: 0.5 CPU cores, 1 Gi memory

Environment variables (This is key)

Name    Value

API_URL https://fastapi-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io


🔹 Step 4 — Ingress 

Scroll down to Ingress settings:

Enable ingress: Checked

Ingress traffic: Accepting traffic from Anywhere

Target port: 8501

Click: Review + Create

We can then allow Azure to validate the resource and click Create once the validation is successful.
After the deployment is complete, we can select the frontend (Streamlit) URL to access our application.

![Streamlit Screenshots](https://raw.githubusercontent.com/ken1711/electricity_load_forecast/main/streamlit/streamlit.png)

[Streamlit Frontend Cloud URL:](https://streamlit-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io)


### Live Cloud links (Live Demo):

Final result you’ll get:

FastAPI Backend:
https://fastapi-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io

Swagger API Docs:
https://fastapi-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io/docs

Streamlit Frontend:
https://streamlit-app.greenhill-0fd68809.germanywestcentral.azurecontainerapps.io


## 🛠️Tech Stack

| Layer       | Technology|
| :--------------| :----------|
| Language          | Python 3.13| 
| Data Source | ENTSO-E Mendeley Data|
| ML Model            | XGBoost Regression, Pandas, NumPy, Scikit-learn| 
| Backend API     | FastAPI + Uvicorn|       
| Frontend   | Streamlit|  
| Containerization       | Docker| 
| Cloud | Azure Container Apps|


## 🧪 Future Work

What can be improved:

- Add additional features, such as weather forecast data or integration with solar radiation data to improve model accuracy.
- Explore advanced models, including LSTM, Transformers, or other deep learning approaches.
- Improve hyperparameter tuning to further optimize model performance.


## 📚 References
- [Mendeley Dataset](https://data.mendeley.com/datasets/ybggkc58fz/1)

- [Sciki-Learn Documentaion](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html#sklearn.ensemble.HistGradientBoostingRegressor)

- [XGBoost Documentation](https://xgboost.readthedocs.io/en/latest/python/sklearn_estimator.html)

- [FastAPI Documentation](https://fastapi.tiangolo.com/tutorial/)

- [Streamlit Documentation](https://docs.streamlit.io/)

- [Docker Documentation](https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/)

- [Azure Cloud](https://learn.microsoft.com/en-us/azure/container-apps/overview)


## 📜 License

This project is released under the MIT License.


## 📬Contact

Github: https://github.com/ken1711
                           
