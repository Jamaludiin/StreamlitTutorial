import streamlit as st
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.chat_message(name, *, avatar=None)
st.subheader("1: Example of st.chat_message")


with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))


# without using the with statement
mesg = st.chat_message("user")
mesg.write("Hello 👋")
mesg.line_chart(np.random.randn(30, 3))
mesg.subheader("This is part is part of the message")
mesg.title("This is a title")

st.subheader("This is part is out of the message")
