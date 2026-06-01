# FILE: smart_rice_system/pages/7_Warehouse_Dashboard.py
import streamlit as st

st.title("🏢 Module 7: Warehouse Inventory Allocation Dashboard")

c1, c2, c3 = st.columns(3)
c1.metric("Current Stock (Godown G1)", "245 Tons")
c2.metric("Available Space Remaining", "255 Tons")
c3.metric("Total Occupancy Rate", "49%")

st.markdown("---")
st.subheader("📦 Stock Level Overview")
st.bar_chart({"Basmati": 120, "Non-Basmati": 85, "Sona Masuri": 40})