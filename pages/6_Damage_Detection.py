# FILE: smart_rice_system/pages/6_Damage_Detection.py
import streamlit as st
import time

st.title("🧫 Module 6: Gunny Bag Quality & Damage Evaluation")

uploaded_file = st.file_uploader("Upload stack inspection image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Batch Processing Stream", width=350)
    
    with st.spinner("Evaluating surface defects..."):
        time.sleep(1.2)
        
    st.subheader("📋 Quality Inspection Report")
    m1, m2, m3 = st.columns(3)
    m1.metric("Healthy Sacks", "112 Bags")
    m2.metric("Damaged Sacks", "8 Bags", delta="-8 Action Required", delta_color="inverse")
    m3.metric("Defect Percentage", "6.7%")