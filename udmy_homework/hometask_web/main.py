import streamlit as st
import pandas

st.set_page_config(layout="wide")

content = """
Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured (particularly procedural), 
object-oriented and functional programming. It is often described as a "batteries included" 
language due to its comprehensive standard library."""

st.header("THE BEST COMPANY")
st.write(content)
st.subheader("Our team")


col1, col2, col3 = st.columns(3)


df = pandas.read_csv("data-2.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images-2/" + row['image'])


with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images-2/" + row['image'])


with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images-2/" + row['image'])

