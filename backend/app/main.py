from fastapi import FastAPI
from app.api.v1 import router as v1
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Early Detection: Soil Degradation API",
              description="API for NDVI-based early detection of soil degradation",
              version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(v1, prefix="/api/v1")

@app.get("/")
def root():
    return {"msg": "Early Detection API running", "version": "0.1.0"}
