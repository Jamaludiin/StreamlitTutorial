import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.area_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)

st.subheader("1: Example of st.area_chart")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

area_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(area_chart,hide_index=False)

st.subheader("Dont Specify any column names")
st.area_chart(area_chart)

# draw specific columns
st.subheader("Using the X and Y axis as the column names")
st.area_chart(area_chart, x="Score 1",y="Score 2",color="#ffaa00")
