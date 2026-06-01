# FILE: smart_rice_system/pages/8_Rainfall_Alert.py
import streamlit as st

st.title("🌧️ Module 8: Weather Alert Prevention System")
st.markdown("Predictive microclimate tracking system to shield open-air inventory.")

# Sidebar parameter manipulation slider
rain_prob = st.slider("Simulated Precipitation Probability (%)", min_value=0, max_value=100, value=75)

st.subheader("🚨 Core Weather Monitoring Console")

# Logical matrix rule
if rain_prob > 70:
    st.error("🚨 CRITICAL WEATHER ALERT: Heavy Rainfall Expected within 30 Minutes!")
    st.markdown("""
    **🚨 Automated Mitigation Directives Triggered:**
    * 🛑 Halt all open-air truck unloading activities at Docks 1 and 2 immediately.
    * 🎪 Deploy waterproof tarpaulin sheets over all incoming staging yards.
    * 🚚 Reroute en-route transports to covered holding sheds.
    """)
else:
    st.success("☀️ System Status: Clear skies. Open-air gate operations safe to continue.")