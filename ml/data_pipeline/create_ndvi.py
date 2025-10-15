import numpy as np
from rasterio import open as ropen

def band_to_array(path):
    with ropen(path) as src:
        return src.read(1).astype('float32')

def create_ndvi(nir_path, red_path, out_path):
    nir = band_to_array(nir_path)
    red = band_to_array(red_path)
    denom = (nir + red)
    denom[denom == 0] = 1e-5
    ndvi = (nir - red)/denom
    np.save(out_path, ndvi)
    print("Saved NDVI to", out_path)
