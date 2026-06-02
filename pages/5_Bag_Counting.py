import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np
import os
import requests

# Set a persistent path for the model
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "best.pt")
# REPLACE THIS URL with your actual public link (e.g., Google Drive, GitHub Release, or Dropbox)
MODEL_URL = "YOUR_DIRECT_DOWNLOAD_LINK_HERE" 

@st.cache_resource
def get_model():
    # Ensure folder exists
    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)
        
    # Download model if not exists
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model weights..."):
            response = requests.get(MODEL_URL)
            with open(MODEL_PATH, 'wb') as f:
                f.write(response.content)
    
    return YOLO(MODEL_PATH)

# Load model
model = get_model()

# ... rest of your Streamlit code ...