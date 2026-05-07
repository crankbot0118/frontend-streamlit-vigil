import streamlit as st

st.set_page_config(layout="wide")
st.title("POC Concept for Vigil")

action_box,output_box=st.columns(2,border=True)

with action_box:
    task_select=st.selectbox("Select Task","pre_health_checks",width="stretch")
    
    instance_select=st.selectbox("Select Instance",("cust_instance1","cust_instance2"),width="stretch")
    st.button("Run", type="primary")

with output_box:
        st.title("output")
        container = st.container(height=600,border=False)
        with container:
            st.code("output", language="bash",height="stretch")