import numpy as np
from tensorflow.keras.models import load_model
from app.core.config import settings
import os

class NDVIModel:
    def __init__(self, model_path: str = None):
        self.model_path = model_path or settings.MODEL_PATH
        self.model = None
        if os.path.exists(self.model_path):
            self.load(self.model_path)

    def load(self, path):
        self.model = load_model(path)
        print(f"Loaded model from {path}")

    def predict_patch(self, ndvi_patch: np.ndarray):
        arr = ndvi_patch.astype('float32')
        if arr.ndim == 3:
            arr = np.expand_dims(arr, 0)
        return self.model.predict(arr)
