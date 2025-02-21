import os
import numpy as np
import pydicom
import cv2

SAGITTAL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "myscan", "sagittal")
AXIAL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "myscan", "axial")
CORONAL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "myscan", "coronal")

def get_slices(dir):
    if not os.path.exists(dir):
        pass

    print(dir)

    dicom_files = sorted([f for f in os.listdir(dir)])
    slices = []

    for file in dicom_files:
        dicom_path = os.path.join(dir, file)
        dicom_img = pydicom.dcmread(dicom_path)
        img_array = dicom_img.pixel_array.astype(np.float32)
        img_array = cv2.resize(img_array, (256, 256))
        slices.append(img_array)

    slices = np.array(slices) / 255.0

    print(f"Converted DICOM Shape: {slices.shape}")

SAGITTAL_SLICES = get_slices(SAGITTAL_DIR)
AXIAL_SLICES = get_slices(AXIAL_DIR)
CORONAL_SLICES = get_slices(CORONAL_DIR)

np.save("data/myscan/sagittal.npy", SAGITTAL_SLICES)
np.save("data/myscan/axial.npy", AXIAL_SLICES)
np.save("data/myscan/coronal.npy", CORONAL_SLICES)

print("Scans saved as npy files!")