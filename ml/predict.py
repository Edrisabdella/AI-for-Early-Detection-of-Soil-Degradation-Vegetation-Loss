import argparse
import numpy as np
from tensorflow.keras.models import load_model

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--ndvi", required=True)
    args = p.parse_args()
    model = load_model(args.model)
    ndvi = np.load(args.ndvi)
    if ndvi.ndim == 2:
        ndvi = np.expand_dims(ndvi, 0)
    if ndvi.ndim == 3:
        ndvi = np.expand_dims(ndvi, -1)
    preds = model.predict(ndvi)
    print(preds)
