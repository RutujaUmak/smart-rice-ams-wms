import streamlit as st
import cv2
import numpy as np
import os
import requests
from ultralytics import YOLO

# 1. Configuration
MODEL_PATH = 'models/best.pt'
# REPLACE WITH YOUR PUBLICLY ACCESSIBLE DIRECT DOWNLOAD LINK
# (e.g., from a GitHub Release or direct storage link)
MODEL_URL = "YOUR_DIRECT_DOWNLOAD_URL_HERE" 

# 2. Robust Model Loader
@st.cache_resource
def get_model():
    if not os.path.exists(MODEL_PATH):
        os.makedirs('models', exist_ok=True)
        with st.spinner("Downloading model weights..."):
            response = requests.get(MODEL_URL)
            with open(MODEL_PATH, 'wb') as f:
                f.write(response.content)
    return YOLO(MODEL_PATH)

# 3. Streamlit Interface
st.title("Module 5: Gunny Bag Counting & Quality")
model = get_model()

uploaded_file = st.file_uploader("Upload an unloading bay snapshot...", type=["jpg", "png"])

if uploaded_file:
    # Process Image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Prediction
    results = model.predict(source=img, conf=0.3)
    
    # Analytics Logic
    quality_counts = {'Healthy': 0, 'Damaged': 0, 'Wet': 0, 'Torn': 0}
    
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in quality_counts:
                quality_counts[label] += 1
                
    # Display UI
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Healthy", quality_counts['Healthy'])
    col2.metric("Damaged", quality_counts['Damaged'])
    col3.metric("Wet", quality_counts['Wet'])
    col4.metric("Torn", quality_counts['Torn'])
    
    st.image(results[0].plot(), caption="Detection Results", use_column_width=True)