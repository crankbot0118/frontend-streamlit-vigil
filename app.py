import streamlit as st

st.set_page_config(layout="wide")
st.title("POC Concept for Vigil")

action_box,output_box=st.columns(2,border=True)

with action_box:
    task_select,instance_select,progress=st.columns(3,border=True,vertical_alignment="bottom")

with output_box:
    st.title("output")
    txt=st.text_area("andncnsndjncjsdnclw")