import streamlit as st
import pandas as pd


# st.columns(spec, *, gap="small")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
   st.title("This is a TITLE of COLUMN ONE")
   st.header("This is a HEADER")
   st.subheader("This is SUBHEADER")
   st.write("This is a WRITE")

with col2:
    st.title("This is a TITLE of COLUMN TWO")
    st.checkbox("This CheckBox")
    st.multiselect("This CheckBox",['A','B','C','D'])

with col3:
   st.title("This is a TITLE of COLUMN THREE")
   st.header("Another HEADER")
   st.button("Button")