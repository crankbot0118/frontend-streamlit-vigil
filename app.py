import streamlit as st

st.set_page_config(layout="wide")

st.title("System Monitor")

st.divider()

col1, col2, col3 = st.columns(3,
vertical_alignment="bottom")

with col1:
    st.metric("CPU Usage", "24%", delta="Load Avg:
0.45")

with col2:
    st.metric("Memory Used", "3.2 GB", delta="-12 GB
free")

with col3:
    st.metric("Disk Usage", "68%", delta="120 GB
free")