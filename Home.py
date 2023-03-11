import streamlit as st
import pandas
import functions

st.set_page_config(layout="centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Solomon Asiedu-Ofei Jnr :wave:")
    content = """Self-directed and driven Project Professional who doubles as a Data Analyst and Python Programmer with a strong passion for making data-driven decisions in the project environment. 
                ."""
    
    st.info(content)

content2 = """I strive to deliver excellent results and performance whiles translating my experience, knowledge, skills, and abilities into value wherever I find myself.
                Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.info(content2)

st.markdown("---")

df = pandas.read_csv("data.csv", sep=";")

my_grid = functions.make_grid(10,2)

for index, row in df[:10].iterrows():
    my_grid[0][0].header(row["title"])
    my_grid[0][0].write(row["description"])
    my_grid[0][0].image("images/" + row["image"])
    my_grid[0][0].write(f"[Source Code]({row['url']})")

for index, row in df[10:].iterrows():    
    my_grid[0][1].header(row["title"])
    my_grid[0][1].write(row["description"])  
    my_grid[0][1].image("images/" + row["image"])
    my_grid[0][1].write(f"[Source Code]({row['url']})")
     

'''
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
'''