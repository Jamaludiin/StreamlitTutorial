import streamlit as st
from datetime import time
from datetime import datetime

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.slider")

bet_price = st.slider("How much are you going to plan to bet", 5, 500, 10)
st.write("I want to pay", bet_price, "$")

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.slider")

bet_price = st.slider("How much are you going to plan to bet", 5, 500, 10)
st.write("I want to pay", bet_price, "$")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("2: Example of st.slider with range values")

values = st.slider(
    label = 'Select a range of values you want to bet',
    min_value= 0.0, 
    max_value= 200.0, 
    value= (25.0, 75.0),
    step= 2.0
    )

st.write('Values:', values)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.slider with range values")

values = st.slider(
    label = 'Select a range of values you want to bet',
    min_value= 0.0, 
    max_value= 200.0, 
    value= (25.0, 75.0),
    step= 2.0
    )

st.write('Values:', values)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("3: Example of st.slider with time")

appointment = st.slider(
    "Book a Doctor at the hostpital:",
    value=(time(11, 30), time(12, 45)))

st.write("You're scheduled for:", appointment)

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
from datetime import time

st.subheader("3: Example of st.slider with time")

appointment = st.slider(
    "Book a Doctor at the hostpital:",
    value=(time(11, 30), time(12, 45)))

st.write("You're scheduled for:", appointment)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("4: Example of st.slider with datetime")
start_time = st.slider(
    "When do you start this job (date and time)?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)



#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
from datetime import datetime

st.subheader("4: Example of st.slider with datetime")
start_time = st.slider(
    "When do you start this job (date and time)?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
"""
my_code(code_example)
st.divider()