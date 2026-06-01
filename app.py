# FILE: smart_rice_system/app.py
import streamlit as st

st.set_page_config(
    page_title="Smart Rice Dashboard Engine",
    page_icon="🌾",
    layout="wide"
)

st.title("🌾 Smart Rice Gate Operations & Storage Management Engine")
st.markdown("---")

st.markdown("""
### 🚜 End-to-End AMS & WMS Prototype Core Ecosystem
Welcome to the central command hub. Select an operation from the sidebar navigation menu to track arrivals, run machine learning quality audits, or verify warehouse capacity allocation.
""")

col1, col2, col3 = st.columns(3)
col1.metric("Prototype Workflow Environment", "Fully Integrated")
col2.metric("Computer Vision Nodes", "YOLO Enabled (Module 5 & 6)")
col3.metric("System Configuration Status", "Active Core Engine")

st.info("💡 Navigation Tip: Follow the sequential numbering in the left sidebar menu to simulate a real load of incoming rice moving through the facility workflow.")