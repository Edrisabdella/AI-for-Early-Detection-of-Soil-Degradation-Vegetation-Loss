from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.models.model import NDVIModel
from app.utils.raster_utils import compute_ndvi
import numpy as np
import rasterio

router = APIRouter()
model = NDVIModel()

@router.post("/predict/ndvi-patch")
async def predict_ndvi_patch(nir: UploadFile = File(...), red: UploadFile = File(...)):
    try:
        nir_bytes = await nir.read()
        red_bytes = await red.read()
        with rasterio.MemoryFile(nir_bytes) as nf, rasterio.MemoryFile(red_bytes) as rf:
            with nf.open() as nsrc, rf.open() as rsrc:
                nir_arr = nsrc.read(1).astype('float32')
                red_arr = rsrc.read(1).astype('float32')
                ndvi = compute_ndvi(nir_arr, red_arr)
                if ndvi.shape != (64,64):
                    ndvi_patch = np.resize(ndvi, (64,64))
                else:
                    ndvi_patch = ndvi
                ndvi_patch = np.expand_dims(ndvi_patch, -1)
                preds = model.predict_patch(ndvi_patch)
                return JSONResponse({"risk_score": float(preds[0][0])})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
