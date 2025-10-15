"""Simple raster utilities to compute NDVI and read rasters."""
import numpy as np
import rasterio
from rasterio.enums import Resampling

def read_band(path, rescale=None):
    with rasterio.open(path) as src:
        arr = src.read(1, resampling=Resampling.bilinear).astype("float32")
        if rescale:
            arr = arr / rescale
        return arr, src.profile

def compute_ndvi(nir_band, red_band):
    denom = (nir_band + red_band)
    denom[denom == 0] = 1e-5
    ndvi = (nir_band - red_band) / denom
    return ndvi