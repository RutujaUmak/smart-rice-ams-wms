# FILE: smart_rice_system/pages/1_Farmer_Booking.py
import streamlit as st

st.title("🚜 Module 1: Farmer Registration & Slot Booking")

with st.form("booking_form"):
    st.subheader("📝 Record New Delivery Intent")
    name = st.text_input("Farmer Name", value="Ravi")
    village = st.text_input("Village", value="Village A")
    rice_type = st.selectbox("Rice Type", ["Basmati", "Non-Basmati", "Sona Masuri"])
    acres = st.number_input("Cultivated Size (Acres)", min_value=1, value=5)
    
    submitted = st.form_submit_button("Forecast Yield & Book Slot")

if submitted:
    # Rule-based simulation calculations matching roadmap
    expected_yield = acres * 1.2
    required_bags = acres * 24
    
    st.success(f"✅ Slot provisionally scheduled for Farmer {name}!")
    
    c1, c2 = st.columns(2)
    c1.metric("Predicted Yield Output", f"{expected_yield:.1f} Tons")
    c2.metric("Required Gunny Bags", f"{required_bags} Units")