import streamlit as st
import pandas as pd

st.title("การทดสอบสร้างเว็ปด้วยPython")
st.image("R.jpg")
st.header("การนำเสนอข้อมูลกราฟด้วยPython")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("./img/800px-Iris_versicolor_3.jpg")

with col2:
    st.header("Verginica")
    st.image("./img/Iris_virginica.jpg")

with col3:
    st.header("Setosa")
    st.image("./img/661px-Iris_setosa_2.jpg")

df=pd.read_csv("./data/iris.cv")
st.write(df.head(10))