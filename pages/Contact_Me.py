import streamlit as st
import pandas
import functions

st.set_page_config(layout="wide")

st.header("Contact Us :smile:")


with st.form(key="email_form"):
    user_email = st.text_input(" ", placeholder="Your email adresss")
    raw_message = st.text_area(" ", placeholder="Your Message goes here") 
    
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button()
    if button:
        functions.send_email(message)
        st.info("Your email was sent successfully")