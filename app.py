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

col1, col2 = st.columns(2)

with col1:
    st.write("Top of Column 1")
    st.button("Bottom of Column 1")
