import streamlit as st
from ultralytics import YOLO
from pathlib import Path
import numpy as np
import cv2

# --------------------------------
# PAGE CONFIG
# --------------------------------
st.set_page_config(
    page_title="Gunny Bag Counting",
    page_icon="📦",
    layout="wide"
)

# --------------------------------
# MODEL PATH
# --------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best.pt"

# --------------------------------
# LOAD MODEL
# --------------------------------
@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        st.error(f"Model not found:\n{MODEL_PATH}")
        st.stop()

    return YOLO(str(MODEL_PATH))


model = load_model()

# --------------------------------
# TITLE
# --------------------------------
st.title("📦 Gunny Bag Counting System")

st.write("Upload an image to count gunny bags.")

# --------------------------------
# FILE UPLOADER
# --------------------------------
uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

# --------------------------------
# PREDICTION
# --------------------------------
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
            conf=0.80,
            iou=0.40,
            verbose=False
        )

    result = results[0]

    # --------------------------------
    # COUNT ONLY HIGH-CONFIDENCE BAGS
    # --------------------------------
    total_bags = 0

    img = image.copy()

    st.subheader("Detection Details")

    count = 1

    for box in result.boxes:

        confidence = float(box.conf[0])

        if confidence >= 0.80:

            total_bags += 1

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            cv2.rectangle(
                img,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

            cv2.putText(
                img,
                f"Bag {count} ({confidence:.2f})",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            st.write(
                f"Bag {count} | Confidence = {confidence:.2f}"
            )

            count += 1

    # --------------------------------
    # SHOW COUNT
    # --------------------------------
    st.success(
        f"Total Gunny Bags Detected: {total_bags}"
    )

    st.metric(
        label="📦 Total Bags",
        value=total_bags
    )

    # --------------------------------
    # SHOW RESULT IMAGE
    # --------------------------------
    st.subheader("Detection Result")

    st.image(
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
        use_container_width=True
    )

# --------------------------------
# DEBUG INFO
# --------------------------------
with st.expander("Debug Info"):

    st.write("Model Path:", MODEL_PATH)
    st.write("Model Exists:", MODEL_PATH.exists())

    if MODEL_PATH.exists():
        st.write("Classes:", model.names)