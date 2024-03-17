import streamlit as st


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
