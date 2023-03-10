import streamlit as st

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Solomon Asiedu-Ofei Jnr :wave:")
    content = """Self-directed and driven Project Professional who doubles as a Data Analyst and Python Programmer with a strong passion for making data-driven decisions in the project environment. 
                I strive to deliver excellent results and performance whiles translating my experience, knowledge, skills, and abilities into value wherever I find myself."""
    
    st.info(content)
