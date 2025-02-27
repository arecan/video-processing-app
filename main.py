import streamlit as st
from gui import setup_sidebar, display_video

# Titre de l'application
st.title("🎥 Tableau de Bord de Traitement Vidéo en Temps Réel")

# Configuration de la barre latérale et récupération des paramètres utilisateur
effect, params = setup_sidebar()

# Lancement de la capture vidéo et affichage des traitements en temps réel
display_video(effect, params)
