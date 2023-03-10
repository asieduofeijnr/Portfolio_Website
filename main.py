import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Solomon Asiedu-Ofei Jnr :wave:")
    content = """Self-directed and driven Project Professional who doubles as a Data Analyst and Python Programmer with a strong passion for making data-driven decisions in the project environment. 
                I strive to deliver excellent results and performance whiles translating my experience, knowledge, skills, and abilities into value wherever I find myself."""
    
    st.info(content)

content2 = """Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        #image_name = st.write(row["image"])
        #st.image(f"images/{image_name}")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])