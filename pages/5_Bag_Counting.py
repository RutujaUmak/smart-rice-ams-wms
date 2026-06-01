import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import os

st.set_page_config(page_title="Gunny Bag Counting Engine", page_icon="📊", layout="wide")

st.title("🧮 Module 5: Gunny Bag Automated Counting")
st.write("Upload an unloading bay snapshot to verify incoming bag counts against booking expectations.")

# 1. Direct path to your custom ONNX model file in the root directory
MODEL_PATH = "best.onnx"

@st.cache_resource
def load_yolo_model():
    if not os.path.exists(MODEL_PATH):
        st.warning(f"⚠️ Custom weights '{MODEL_PATH}' not found in root. Falling back to default YOLOv8n for simulation.")
        return YOLO("yolov8n.pt", task="detect")
    else:
        return YOLO(MODEL_PATH, task="detect")

model = load_yolo_model()

# 2. Split UI Layout Panels
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📸 Upload Ingestion Frame")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    expected_count = st.number_input("Expected Bags (From Invoice Manifest)", min_value=1, value=120)

with col2:
    st.subheader("🎯 Core Engine Analytics")
    
    if uploaded_file is not None:
        # Read uploaded browser bytes straight into an OpenCV array
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_img = cv2.imdecode(file_bytes, 1)
        
        with st.spinner("Processing image via YOLO Object Detection..."):
            # Run inference prediction using your verified parameters
            results = model.predict(source=opencv_img, conf=0.25)
            
            # Extract counting metric arrays
            detected_count = len(results[0].boxes)
            variance = detected_count - expected_count
            
            # Draw bounding boxes and map back to safe RGB space
            res_plotted = results[0].plot()
            res_rgb = cv2.cvtColor(res_plotted, cv2.COLOR_BGR2RGB)
            
        st.success("Analysis Complete!")
        
        # Display live calculation statistics cards
        m1, m2, m3 = st.columns(3)
        m1.metric("Expected Bags", f"{expected_count}")
        m2.metric("Detected Bags (YOLO)", f"{detected_count}")
        
        if variance < 0:
            m3.metric("Discrepancy Variance", f"{variance}", delta=f"{abs(variance)} Missing Sacks", delta_color="inverse")
        else:
            m3.metric("Discrepancy Variance", f"+{variance}" if variance > 0 else "0", delta="Match Verified")
            
        # Display the live AI output image
        st.image(res_rgb, caption=f"Processed Image: {detected_count} Sacks Counted", use_container_width=True)
    else:
        st.info("💡 Waiting for an unloading bay photo to trigger calculation metrics.")