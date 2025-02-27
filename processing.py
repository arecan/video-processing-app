import cv2
import numpy as np

def apply_canny(image, low_threshold, high_threshold):
    """Applique l'algorithme de détection des contours de Canny."""
    return cv2.Canny(image, low_threshold, high_threshold)

def apply_background_subtraction(image, bg_subtractor):
    """Applique la soustraction d’arrière-plan."""
    return bg_subtractor.apply(image)

def apply_color_filter(image, lower_bound, upper_bound):
    """Filtrage d'une couleur spécifique en HSV."""
    hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    return cv2.bitwise_and(image, image, mask=mask), mask
