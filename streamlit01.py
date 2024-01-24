import streamlit as st

st.title("การทดสอบสร้างเว็ปด้วยPython")
st.image("R.jpg")
st.header("การนำเสนอข้อมูลกราฟด้วยPython")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("https://en.m.wikipedia.org/wiki/File:Iris_versicolor_3.jpg")

with col2:
    st.header("Verginica")
    st.image("https://en.m.wikipedia.org/wiki/File:Iris_virginica.jpg")

with col3:
    st.header("Setosa")
    st.image("https://species.m.wikimedia.org/wiki/File:Iris_setosa_2.jpg")