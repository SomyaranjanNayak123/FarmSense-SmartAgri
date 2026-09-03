import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_NAME = os.getenv("APP_NAME", "SmartAgri")
    SECRET_KEY = os.getenv("SECRET_KEY", "smartagri_super_secret_key_2024")
    DEBUG = os.getenv("DEBUG", "True") == "True"

    # MongoDB - uses local by default (no auth needed for dev)
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/smart_agri")

    # APIs (optional - app works without them using mock data)
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
    SATELLITE_API_KEY = os.getenv("SATELLITE_API_KEY", "")
    MARKET_API_KEY = os.getenv("MARKET_API_KEY", "")

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "")
    FROM_EMAIL = os.getenv("FROM_EMAIL", "noreply@smartagri.com")

    JWT_SECRET = os.getenv("JWT_SECRET", "smartagri_jwt_secret_key_2024")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

config = Config()
