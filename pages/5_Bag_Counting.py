import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

# Load your model (ensure path is correct)
model = YOLO('models/best.pt') 

st.title("Module 5 & 6: Gunny Bag Analysis")

uploaded_file = st.file_uploader("Upload an unloading bay snapshot...", type=["jpg", "png"])

if uploaded_file:
    # Read image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    
    # Run prediction
    results = model.predict(source=img, conf=0.25)
    
    # Analyze results
    quality_counts = {'Healthy': 0, 'Damaged': 0, 'Wet': 0, 'Torn': 0}
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            if label in quality_counts:
                quality_counts[label] += 1
                
    # Display analytics
    st.write("### Core Engine Analytics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Healthy", quality_counts['Healthy'])
    col2.metric("Damaged", quality_counts['Damaged'])
    col3.metric("Wet", quality_counts['Wet'])
    col4.metric("Torn", quality_counts['Torn'])
    
    # Show annotated image
    st.image(results[0].plot(), caption="Annotated Detection Result", use_column_width=True)