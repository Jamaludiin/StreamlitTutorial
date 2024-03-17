import streamlit as st
import time


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.balloons()

st.subheader("1: Example of st.balloons")

if st.button("Do you like Banana"):
    st.balloons()
else:
    time.sleep(20)
    st.toast("OH SORRY FOR THAT", icon="😍")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import time

st.subheader("1: Example of st.balloons")

if st.button("Do you like Banana"):
    st.balloons()
else:
    time.sleep(20)
    st.toast("OH SORRY FOR THAT", icon="😍")

"""
my_code(code_example)
st.divider()