import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")

st.subheader("1: Example of st.metric")

st.metric(label="Accuracy", value="90.5 Acc", delta="0.5 Err", delta_color='normal',help="AI Accuracy for the model")

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.metric")

st.metric(label="Accuracy", value="90.5 Acc", delta="0.5 Err", delta_color='normal',help="AI Accuracy for the model")

"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")

st.subheader("2: Example of st.metric")
progress_df = pd.DataFrame(
    {
    "Main Score1":
               [99,100,100,84,99,88],
    "Score 2": 
               [0.4,0.-5,5.5,2.-4,8.0,2.6], 
    "Main Score2": 
                [88,99,88,55,77,56],
     "Score 3": 
                [0.2,-0.7,4.5,-1.7,9.0,-1.6], 

    }
   
)
col1,col2 = st.columns(2)

with col1:
    for index, row in progress_df.iterrows():
        st.metric(
            label="Accuracy Points",
            value=str(row["Main Score1"]),
            delta=str(row["Score 2"]),
            delta_color="normal",
            help="AI Accuracy for the model",
        )

with col2:
    for index, row in progress_df.iterrows():
        st.metric(
            label="Accuracy Points",
            value=str(row["Main Score2"]),
            delta=str(row["Score 3"]),
            delta_color="normal",
            help="AI Accuracy for the model",
        )

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st

st.subheader("2: Example of st.metric")
progress_df = pd.DataFrame(
    {
    "Main Score1":
               [99,100,100,84,99,88],
    "Score 2": 
               [0.4,0.-5,5.5,2.-4,8.0,2.6], 
    "Main Score2": 
                [88,99,88,55,77,56],
     "Score 3": 
                [0.2,-0.7,4.5,-1.7,9.0,-1.6], 

    }
   
)
col1,col2 = st.columns(2)

with col1:
    for index, row in progress_df.iterrows():
        st.metric(
            label="Accuracy Points",
            value=str(row["Main Score1"]),
            delta=str(row["Score 2"]),
            delta_color="normal",
            help="AI Accuracy for the model",
        )

with col2:
    for index, row in progress_df.iterrows():
        st.metric(
            label="Accuracy Points",
            value=str(row["Main Score2"]),
            delta=str(row["Score 3"]),
            delta_color="normal",
            help="AI Accuracy for the model",
        )
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")

st.subheader("3: Example of st.metric")
col1, col2, col3 = st.columns(3)
col1.metric("Sale Price", "45 $", "1.2% Discount")
col2.metric("Anual Price", "99.9 $", "0.01% Discount")
col3.metric("Member Price", str(77)+'$', "6% Low")

#_____________________________________________________________

st.title("3: Code of the Example above")

code_example = """import streamlit as st

st.subheader("3: Example of st.metric")

col1, col2, col3 = st.columns(3)
col1.metric("Sale Price", "45 $", "1.2% Discount")
col2.metric("Anual Price", "99.9 $", "0.01% Discount")
col3.metric("Member Price", str(77)+'$', "6% Low")
"""
my_code(code_example)
st.divider()