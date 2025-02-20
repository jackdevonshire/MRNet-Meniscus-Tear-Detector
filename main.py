import os
import numpy as np
import torch
from torchvision import transforms
import matplotlib.pyplot as plt
import cv2

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "mrnet", "train")

def load_mri_series(patient_id, plane="sagittal"):
    file_path = os.path.join(DATA_DIR, plane, f"{patient_id}.npy")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    series = np.load(file_path)
    return series

sagittal_series = load_mri_series("0100")

plt.imshow(sagittal_series[0], cmap="gray")
plt.show()
