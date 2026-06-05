import streamlit as st
import cv2
import numpy as np
import os
from ultralytics import YOLO

# --- CONFIGURATION ---
# Ensure this path matches the EXACT location of your valid best.pt file
MODEL_PATH = r"C:\Users\ASUS\Documents\AI\smart_rice_system\models\best.pt"

@st.cache_resource
def get_model():
    """Safely load the model, checking if the file is valid."""
    if not os.path.exists(MODEL_PATH):
        st.error(f"Error: Model not found at {MODEL_PATH}")
        return None
    
    # Basic check to ensure file is not a text/html file
    if os.path.getsize(MODEL_PATH) < 1000000:
        st.error("Error: The file 'best.pt' is corrupted or too small. Please replace it with a valid training weight file.")
        return None
    
    try:
        return YOLO(MODEL_PATH)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# --- UI SETUP ---
st.title("Module 5: Gunny Bag Counting & Quality")
model = get_model()

if model:
    uploaded_file = st.file_uploader("Upload an unloading bay snapshot...", type=["jpg", "png"])

    if uploaded_file:
        # Convert image for YOLO
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        # Perform Prediction
        results = model.predict(source=img, conf=0.3)
        
        # Analytics Logic
        quality_counts = {'Healthy': 0, 'Damaged': 0, 'Wet': 0, 'Torn': 0}
        
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                if label in quality_counts:
                    quality_counts[label] += 1
                
        # Display Results
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Healthy", quality_counts['Healthy'])
        col2.metric("Damaged", quality_counts['Damaged'])
        col3.metric("Wet", quality_counts['Wet'])
        col4.metric("Torn", quality_counts['Torn'])
        
        # Show annotated image
        st.image(results[0].plot(), caption="Detection Results", use_column_width=True)
else:
    st.warning("Model failed to load. Please fix the path or file corruption issue in your 'models' folder.")