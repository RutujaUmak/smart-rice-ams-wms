import streamlit as st
import cv2
import numpy as np
import os
from ultralytics import YOLO

# 1. Configuration
# Ensure your model is at: C:\Users\ASUS\Documents\AI\smart_rice_system\models\best.pt
MODEL_PATH = os.path.join(os.getcwd(), 'models', 'best.pt')

@st.cache_resource
def get_model():
    # We use 'r' before the string to handle Windows backslashes correctly
    model_path = r"C:\Users\ASUS\Documents\AI\smart_rice_system\models\best.pt"
    
    # 1. Verify existence
    if not os.path.exists(model_path):
        st.error(f"File not found at: {model_path}. Please check the folder path.")
        return None
    
    # 2. Check if the file is a valid size (A real YOLO model is usually > 5MB)
    if os.path.getsize(model_path) < 1000000:
        st.error("The file 'best.pt' is corrupted (too small). Please replace it with your actual trained model file.")
        return None

    try:
        # Load the model
        model = YOLO(model_path)
        return model
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None
# 2. Page UI
st.title("Module 5: Gunny Bag Counting & Quality")
model = get_model()

if model:
    uploaded_file = st.file_uploader("Upload an unloading bay snapshot...", type=["jpg", "png"])

    if uploaded_file:
        # Convert uploaded file to OpenCV format
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        
        # Prediction
        results = model.predict(source=img, conf=0.3)
        
        # Analytics Logic
        quality_counts = {'Healthy': 0, 'Damaged': 0, 'Wet': 0, 'Torn': 0}
        
        # Count detections
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                if label in quality_counts:
                    quality_counts[label] += 1
                
        # Display Metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Healthy", quality_counts['Healthy'])
        col2.metric("Damaged", quality_counts['Damaged'])
        col3.metric("Wet", quality_counts['Wet'])
        col4.metric("Torn", quality_counts['Torn'])
        
        # Display Image
        st.image(results[0].plot(), caption="Detection Results", use_column_width=True)