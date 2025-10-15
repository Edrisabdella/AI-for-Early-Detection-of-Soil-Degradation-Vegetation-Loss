import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    MODEL_PATH: str = os.getenv("MODEL_PATH", "/app/models/ndvi_model.h5")
    MAPBOX_TOKEN: str = os.getenv("MAPBOX_TOKEN", "")
    DATA_DIR: str = os.getenv("DATA_DIR", "/data")

settings = Settings()
