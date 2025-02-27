import cv2
import numpy as np

def rgb_to_hsv(r, g, b):
    """Convertit une couleur RGB en HSV."""
    hsv_color = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
    return hsv_color
