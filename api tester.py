import streamlit as st
import requests

st.title("API Data Submitter")

with st.form("my_form"):
    user_input = st.text_input("Enter message")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        url = "https://54.198.10.240:8000"
        payload = {"message": user_input}
        
        # Sending the POST request
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            st.success("Data sent successfully!")
        else:
            st.error(f"Failed to send data: {response.status_code}")
