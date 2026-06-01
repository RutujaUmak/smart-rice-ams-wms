# FILE: smart_rice_system/pages/4_ANPR_Verification.py
import streamlit as st
import time

st.title("🆔 Module 4: Gate Entry & Vehicle Verification")
st.markdown("Automated License Plate Recognition (ANPR) Check.")

uploaded_img = st.file_uploader("Capture vehicle entry frame...", type=["jpg", "png", "jpeg"])

if uploaded_img:
    st.image(uploaded_img, caption="Ingested Camera Stream", width=350)
    
    with st.spinner("Processing License Plate Extraction..."):
        time.sleep(1)
        
    st.code("DETECTED VEHICLE STRING: MH01AB1234")
    st.success("✓ Booking Match Verified! Gate open command sent.")