import streamlit as st

st.set_page_config(layout="wide")
st.title("POC Concept for Vigil")

action_box,output_box=st.columns(2,border=True)

with action_box:
    task_select=st.selectbox("Select Task","pre_health_checks",width="stretch")
    instance_select=st.selectbox("Select Instance",("cust_instance1","cust_instance2"),width="stretch")
    run_clicked = st.button("Run", type="primary")
    if run_clicked:
        url = "http://54.198.10.240:8000/tasks/pre-health-check/execute"
        payload = {"instance_name": instance_select,"task_name": task_select}

with output_box:
        st.title("output")
        container = st.container(height=600,border=False)
        with container:
            st.code("output", language="bash",height="stretch")