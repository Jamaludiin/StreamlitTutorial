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



#------------------------------------------------------------
# syntax 
# st.map(data=None, *, latitude=None, longitude=None, color=None, size=None, zoom=None, use_container_width=True)
st.subheader("2: Example of st.map")
df = pd.DataFrame({
    "col1": np.random.randn(100) / 50 + 37.76,
    "col2": np.random.randn(100) / 50 + -122.4,
    "col3": np.random.randn(100) * 100,
    "col4": np.random.rand(100, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

st.subheader("2: Example of st.map")
df = pd.DataFrame({
    "col1": np.random.randn(100) / 50 + 37.76,
    "col2": np.random.randn(100) / 50 + -122.4,
    "col3": np.random.randn(100) * 100,
    "col4": np.random.rand(100, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')
"""
my_code(code_example)
st.divider()