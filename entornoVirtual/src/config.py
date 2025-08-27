import os
from dotenv import load_dotenv

# Cargar .env si existe
if os.path.exists(".env"):
    load_dotenv()

class Settings:
    ENV: str = os.getenv("ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "changeme")

settings = Settings()
