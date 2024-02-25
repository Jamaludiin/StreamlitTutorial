import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
st.subheader("1: Example of st.number_input")

st.number_input(label="What is your Lucky Number")

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.number_input")

st.number_input(label="What is your Lucky Number")
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
st.subheader("2: Example of st.number_input")
st.number_input(label="What is your age", 
                min_value=1, 
                max_value=100,
                value=10,
                step=2,
                help="Only a number",
                placeholder="Numbers",
                disabled=False,
                label_visibility='visible')

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.number_input")
st.number_input(label="What is your age", 
                min_value=1, 
                max_value=100,
                value=10,
                step=2,
                help="Only a number",
                placeholder="Numbers",
                disabled=False,
                label_visibility='visible')
"""
my_code(code_example)
st.divider()