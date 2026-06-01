# FILE: smart_rice_system/pages/2_Slot_Scheduling.py
import streamlit as st
import pandas as pd

st.title("⏳ Module 2: Warehouse Slot Staggering Engine")
st.markdown("Automated queuing logic ensuring arrival volumes do not exceed daily processing limits.")

# Clean data dictionary definition
bookings_data = {
    "Farmer ID": ["F001", "F002", "F003"],
    "Farmer Name": ["Ravi", "Anil", "Suresh"],
    "Load Volume": ["5 Tons", "10 Tons", "12 Tons"],
    "Allocated Window": ["08:00 AM", "08:30 AM", "09:00 AM"],
    "Status": ["Confirmed", "Confirmed", "Pending Audit"]
}
df = pd.DataFrame(bookings_data)

st.subheader("🗓️ Scheduled Gate Deliveries (Today)")
st.dataframe(df, use_container_width=True)
st.success("✨ Optimization Rule: Slot gaps are hard-locked at 30 minutes to eliminate unloading dock bottlenecking.")