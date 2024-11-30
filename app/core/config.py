from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    APP_NAME = "FastAPI App"
    DEBUG = os.getenv("DEBUG", False)

settings = Settings()
