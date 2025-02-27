import streamlit as st
import cv2
import numpy as np
from processing import apply_canny, apply_background_subtraction, apply_color_filter

def select_color():
    """Sélectionne une couleur et retourne ses bornes HSV."""
    color = st.color_picker("Sélectionner une couleur", "#ff0000")
    r, g, b = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    hsv_color = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
    lower_bound = np.array([hsv_color[0] - 10, 50, 50])
    upper_bound = np.array([hsv_color[0] + 10, 255, 255])
    return lower_bound, upper_bound

def setup_sidebar():
    """Configure la barre latérale et récupère les paramètres utilisateur."""
    effect = st.sidebar.selectbox("Choisir un effet", ["Aucun", "Contours Canny", "Soustraction d'arrière-plan", "Filtrage de couleur"])
    params = {}

    if effect == "Contours Canny":
        params["low_threshold"] = st.sidebar.slider("Seuil bas", 0, 255, 100)
        params["high_threshold"] = st.sidebar.slider("Seuil haut", 0, 255, 200)
    elif effect == "Filtrage de couleur":
        params["lower_bound"], params["upper_bound"] = select_color()

    return effect, params

def display_video(effect, params):
    """Gère la capture vidéo et applique le traitement sélectionné en temps réel."""
    start_button = st.sidebar.button("Démarrer la Capture Vidéo")

    if start_button:
        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        mask_placeholder = st.empty()
        stop_button = st.sidebar.button("Arrêter")
        bg_subtractor = cv2.createBackgroundSubtractorMOG2()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret or stop_button:
                break
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if effect == "Contours Canny":
                frame = apply_canny(frame, params["low_threshold"], params["high_threshold"])
                frame_placeholder.image(frame, channels="GRAY")
            elif effect == "Soustraction d'arrière-plan":
                frame = apply_background_subtraction(frame, bg_subtractor)
                frame_placeholder.image(frame, channels="GRAY")
            elif effect == "Filtrage de couleur":
                filtered_frame, mask = apply_color_filter(frame, params["lower_bound"], params["upper_bound"])
                mask_placeholder.image(mask, caption="Masque de couleur", channels="GRAY")
                frame_placeholder.image(filtered_frame, channels="RGB")
            else:
                frame_placeholder.image(frame, channels="RGB")

        cap.release()
        cv2.destroyAllWindows()
