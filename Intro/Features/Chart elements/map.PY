import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)
st.subheader("1: Example of st.map")

df = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [55.5500, -2.6],
    columns=['lat', 'lon'])

st.map(df)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

st.subheader("1: Example of st.map")

df = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [55.5500, -2.6],
    columns=['lat', 'lon'])

st.map(df)
"""
my_code(code_example)
st.divider()