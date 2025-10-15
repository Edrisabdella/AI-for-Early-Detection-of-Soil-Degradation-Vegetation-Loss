import numpy as np
from skimage.transform import resize

def extract_patches(ndvi_arr, patch_size=64, stride=32):
    h, w = ndvi_arr.shape
    patches = []
    for y in range(0, h - patch_size + 1, stride):
        for x in range(0, w - patch_size + 1, stride):
            p = ndvi_arr[y:y+patch_size, x:x+patch_size]
            patches.append(p)
    return np.array(patches)

def normalize_patches(patches):
    patches = patches.astype('float32')
    patches = np.expand_dims(patches, -1)
    return patches
