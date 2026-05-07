import streamlit as st

st.set_page_config(layout="wide")
st.title("POC Concept for Vigil")

action_box,output_box=st.columns(2,border=True)

with action_box:
    task_select=st.selectbox(label="Select Task",width="stretch")

with output_box:
    st.title("output")
    st.code("adcbjs cjnqec", language="bash")