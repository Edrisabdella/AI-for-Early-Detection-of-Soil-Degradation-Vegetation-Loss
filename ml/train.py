import argparse
import numpy as np
import pandas as pd
from tensorflow.keras import layers, models, optimizers
from ml.data_pipeline.preprocess import extract_patches, normalize_patches
from sklearn.model_selection import train_test_split
import os

def build_model(input_shape=(64,64,1)):
    model = models.Sequential([
        layers.Conv2D(32, 3, activation='relu', input_shape=input_shape),
        layers.MaxPool2D(2),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPool2D(2),
        layers.Conv2D(128, 3, activation='relu'),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=optimizers.Adam(1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def load_dataset(labels_csv):
    df = pd.read_csv(labels_csv)
    X = []
    y = []
    for _, r in df.iterrows():
        ndvi_npy = r['ndvi_path']
        label = r['label']
        if not os.path.exists(ndvi_npy):
            continue
        arr = np.load(ndvi_npy)
        patches = extract_patches(arr, patch_size=64, stride=64)
        patches = normalize_patches(patches)
        X.append(patches)
        y += [label]*patches.shape[0]
    if len(X) == 0:
        raise ValueError("No data found. Create NDVI .npy files and labels CSV.")
    X = np.concatenate(X, axis=0)
    y = np.array(y).astype('float32')
    return X, y

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--labels", required=True, help="CSV with ndvi_path,label")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--out", default="ndvi_model.h5")
    args = parser.parse_args()

    X, y = load_dataset(args.labels)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    model = build_model(input_shape=X_train.shape[1:])
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=args.epochs, batch_size=32)
    model.save(args.out)
    print("Saved model to", args.out)
