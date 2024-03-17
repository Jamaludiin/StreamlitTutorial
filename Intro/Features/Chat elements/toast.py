import streamlit as st
import time


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.toast(body, *, icon=None)

st.subheader("1: Example of st.toast")

name = st.text_input("Write your Name: ")

if name == 'Admin':
    st.toast('Please login the main page as admin to get the points', icon='😍')
else:
    st.toast('You are not an admin to get the points', icon='😍')


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.toast")

name = st.text_input("Write your Name: ")

if name == 'Admin':
    st.toast('Please login the main page as admin to get the points', icon='😍')
else:
    st.toast('You are not an admin to get the points', icon='😍')

"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.toast(body, *, icon=None)

st.subheader("2: Example of st.toast")

user_likes = st.text_input("Tell me what you like:")

if user_likes is not None:
    st.toast('Amazing to hear that you like ',icon='😍')
    time.sleep(.5)
    st.toast('This is awsome ', icon='😍')
    time.sleep(.5)
    st.toast('Enjoy guys with your ', icon='😍')


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import time

st.subheader("2: Example of st.toast")

user_likes = st.text_input("Tell me what you like:")

if user_likes is not None:
    st.toast('Amazing to hear that you like ',icon='😍')
    time.sleep(.5)
    st.toast('This is awsome ', icon='😍')
    time.sleep(.5)
    st.toast('Enjoy guys with your ', icon='😍')
"""
my_code(code_example)
st.divider()