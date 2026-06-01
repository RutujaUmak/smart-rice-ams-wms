# Save this in C:\Users\ASUS\Documents\AI\smart_rice_system\pages\9_SMS_Notifications.py
import streamlit as st

st.title("💬 Module 9: Automated Stakeholder Notification Hub")
st.markdown("Simulate automated SMS text routing updates directly to farmers and haulers.")

st.subheader("Dispatched Gateway Communication Logs")

st.info("""
📟 **SMS SENT SUCCESSFUL** **Recipient:** Farmer Ravi (ID: F001)  
**Message:** *"Hello Ravi, your delivery slot for Basmati has been verified at Gate 1. Total Counted: 118 Bags. Transaction recorded."*
""")

st.info("""
📟 **SMS SENT SUCCESSFUL** **Recipient:** Vehicle Carrier (No: MH01AB1234)  
**Message:** *"Security Clearance Active. Proceed to unloading dock bay 3 for cargo discharge."*
""")