import streamlit as st
from ultralytics import YOLO
from pathlib import Path
import numpy as np
import cv2

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Gunny Bag Counting",
    page_icon="📦",
    layout="wide"
)

# ---------------------------------
# MODEL PATH
# ---------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best.pt"

# ---------------------------------
# LOAD MODEL
# ---------------------------------
@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        st.error(f"Model not found:\n{MODEL_PATH}")
        st.stop()

    return YOLO(str(MODEL_PATH))

model = load_model()

# ---------------------------------
# TITLE
# ---------------------------------
st.title("📦 Gunny Bag Counting System")

st.write("Upload an image to count gunny bags.")

# ---------------------------------
# UPLOAD IMAGE
# ---------------------------------
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

# ---------------------------------
# PREDICTION
# ---------------------------------
if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    st.subheader("Uploaded Image")

    st.image(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        use_container_width=True
    )

    with st.spinner("Detecting Gunny Bags..."):

        results = model.predict(
            source=image,
            conf=0.25,
            verbose=False
        )

    result = results[0]

    # Count bags
    total_bags = len(result.boxes)

    # Draw boxes
    annotated_image = result.plot()

    # ---------------------------------
    # RESULTS
    # ---------------------------------
    st.success(f"Total Gunny Bags Detected: {total_bags}")

    st.metric(
        label="📦 Total Bags",
        value=total_bags
    )

    st.subheader("Detection Result")

    st.image(
        annotated_image,
        channels="BGR",
        use_container_width=True
    )

    # ---------------------------------
    # DETECTION DETAILS
    # ---------------------------------
    if total_bags > 0:

        st.subheader("Detection Details")

        for i, box in enumerate(result.boxes):

            confidence = float(box.conf[0])

            st.write(
                f"Bag {i+1} | Confidence: {confidence:.2f}"
            )

# ---------------------------------
# DEBUG INFO
# ---------------------------------
with st.expander("Debug Info"):

    st.write("Model Path:", MODEL_PATH)
    st.write("Model Exists:", MODEL_PATH.exists())

    if MODEL_PATH.exists():
        st.write("Classes:", model.names)