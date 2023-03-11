import streamlit as st
from email import message
import smtplib, ssl



def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "adwintechnology@gmail.com"
    password = "daiaodqtddanbhtb"

    receiver = "adwintechnology@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)