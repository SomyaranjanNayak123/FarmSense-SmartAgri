# Smart Agriculture System

An AI-powered smart agriculture platform with crop monitoring, disease detection, yield prediction, and market forecasting.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env  # fill in your keys
```

## Run

```bash
# Backend
uvicorn backend.server:app --reload --port 8000

# Frontend
streamlit run frontend/app.py
```

## Features
- Crop Monitoring & Disease Detection
- Soil Analysis
- Weather Forecasting
- Irrigation Management
- Yield Prediction
- Market Price Forecasting
- Pest Detection
- PDF Reports
