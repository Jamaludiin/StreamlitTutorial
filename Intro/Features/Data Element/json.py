import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.json(body, *, expanded=True)

st.subheader("1: Example of st.json")

col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("Normal Data Presented as json format")
    st.json({
        'Mode': 'Toyota',
        'Price': '20000$',
        'Colors': [
            'Yellow',
            'Red',
            'Blue',
            'Maroon',
            'Black',
        ],
    })




var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

with col2:
    st.subheader("Dictionary Data Converted to json")
    st.json(var_dictionaries)





var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43]
}

with col3:
    st.subheader("Array Data Converted to json")
    st.json(var_dic_data_1)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.json")

col1,col2,col3 = st.columns(3)
with col1:
    st.subheader("Normal Data Presented as json format")
    st.json({
        'Mode': 'Toyota',
        'Price': '20000$',
        'Colors': [
            'Yellow',
            'Red',
            'Blue',
            'Maroon',
            'Black',
        ],
    })




var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

with col2:
    st.subheader("Dictionary Data Converted to json")
    st.json(var_dictionaries)





var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43]
}

with col3:
    st.subheader("Array Data Converted to json")
    st.json(var_dic_data_1)
"""
my_code(code_example)
st.divider()