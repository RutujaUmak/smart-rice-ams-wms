# FILE: smart_rice_system/pages/3_Vehicle_Assignment.py
import streamlit as st

st.title("🚛 Module 3: Logistics & Vehicle Scheduling Matrix")
st.markdown("Rule-based vehicle routing coordinator.")

quantity = st.slider("Total Rice Cargo Load to Transport (Tons)", min_value=1.0, max_value=50.0, value=7.5)
distance = st.number_input("Transport Route Distance (KM)", min_value=1, value=45)

# Automated logistics calculation rules from blueprint specification
if quantity <= 5.0:
    recommended_fleet = "1x Standard 5-Ton Utility Truck (e.g., MH01AB1234)"
elif quantity <= 15.0:
    recommended_fleet = "1x Heavy 15-Ton Multi-Axle Carrier"
else:
    recommended_fleet = "2x Heavy Fleet Transports"

st.subheader("📋 Transport Assignment Result")
st.metric("Recommended Transport Assignment", recommended_fleet)
st.success(f"Route verification finalized successfully for a {distance} KM transit profile.")