import streamlit as st
import numpy as np
import pandas as pd


# def
def my_code(code):
    st.code(f"""{code}""")
#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")
st.title("1: Example of st.columns element")

st.subheader("Display and group elements under Columns")

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


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("Display and group elements under Columns")

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
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")
st.subheader("2: Example: Display charts and other data elements under Columns")

col1, col2 = st.columns([3, 1])
data = np.random.randn(100, 5)

col1.subheader("Column one with a chart")
col1.line_chart(data)

col2.subheader("The row Data in clumn two")
col2.write(data)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example: Display charts and other data elements under Columns")

col1, col2 = st.columns([3, 1])
data = np.random.randn(100, 5)

col1.subheader("Column one with a chart")
col1.line_chart(data)

col2.subheader("The row Data in clumn two")
col2.write(data)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")

st.subheader("3: Example: Display charts and other data elements under Columns")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

col1, col2 = st.columns([3, 1])

col1.subheader("Column one with a chart")
col1.line_chart(var_csv_data)

col2.subheader("Clumn two with row Data")
col2.write(var_csv_data)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("3: Example: Display charts and other data elements under Columns")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

col1, col2 = st.columns([3, 1])

col1.subheader("Column one with a chart")
col1.line_chart(var_csv_data)

col2.subheader("Clumn two with row Data")
col2.write(var_csv_data)
"""
my_code(code_example)
st.divider()