import streamlit as st
import datetime


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.time_input(label, value="now", key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", step=0:15:00)

st.subheader("1: Example of st.time_input")

time = st.time_input('When are you comming', datetime.time(10, 30))
st.write('You are comming at:', time)

st.subheader("Without step property")


time1 = st.time_input(label='When are you going back', value=datetime.time(2, 30), step=datetime.timedelta(minutes=15))
st.write('You are going back at:', time1)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import datetime

st.subheader("1: Example of st.time_input")

time = st.time_input('When are you comming', datetime.time(10, 30))
st.write('You are comming at:', time)

st.subheader("Without step property")


time1 = st.time_input(label='When are you going back', value=datetime.time(2, 30), step=datetime.timedelta(minutes=15))
st.write('You are going back at:', time1)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.time_input(label, value="now", key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", step=0:15:00)

st.subheader("2: Example of st.time_input")
