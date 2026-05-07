# import streamlit as st

# st.set_page_config(layout="wide")
# st.title("POC Concept for Vigil")

# # action_box,output_box=st.columns(2,border=True)

# # with action_box:
# #     task_select,instance_select,progress=st.columns(3,border=True,vertical_alignment="bottom")

# # with output_box:
# #     st.title("output")
# #     st.code("adcbjs cjnqec", language="bash")


# left, middle, right = st.columns(3)

# left.text_input("Write something")
# middle.button("Click me", use_container_width=True)
# right.checkbox("Check me")

import streamlit as st

st.set_page_config(layout="wide")

# Create 3 vertical columns
col1, col2, col3 = st.columns(3, vertical_alignment="bottom")

with col1:
    st.subheader("CPU")
    st.code("CPU Usage: 24%\nLoad Avg: 0.45")

with col2:
    st.subheader("Memory")
    st.code("Used: 3.2 GB\nFree: 12 GB")

with col3:
    st.subheader("Disk")
    st.code("Root Usage: 68%\nFree Space: 120 GB")