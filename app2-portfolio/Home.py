import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Alex Grk")
    content = """Hello, I`m Alex.
    Nice to see you!
    How you doing?"""
    st.info(content)



content2 = """ Python is a high-level, general-purpose programming language.
           Its design philosophy emphasizes code readability with the use of significant indentation. 
           """

st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")



with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

