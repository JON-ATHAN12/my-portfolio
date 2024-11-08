import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("static/photo.jpg", use_column_width="auto")

with col2:
    st.title("Jonathan L")
    content = """
    Aspiring Python Programmer \n
    Passionated to work in Real world projects
    
    """
    st.info(content)
    st.link_button("GitHub","https://github.com/dashboard")
    st.link_button("contact me","http://localhost:8501/Contact_Me")


st.divider()
st.html("<p>"
        "<span style='color:indigo; font-family: verdana; font_size:200%' >"
        " <b>Below you can find some of the apps I have build in Python, Feel free to contact me!</b>"
        "</span>"
        "</p>")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"], divider=True)
        st.write(row["description"])
        # st.image("static/img/" + row["image"])
        st.link_button("Source code", row["url"])


with col4:
    for index, row in df[5:].iterrows():
        st.header(row["title"], divider=True)
        st.write(row["description"])
        # st.image("static/img/" + row["image"])
        st.link_button("Source code", row["url"])
