import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.text_input")

book = st.text_input(label='Programming Book', 
                      value='Python Tutorial',
                      help="hit enter after typing compeleted")

st.write('The book I like is', book)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.text_input")

book = st.text_input(label='Programming Book', 
                      value='Python Tutorial',
                      help="hit enter after typing compeleted")

st.write('The book I like is', book)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("2: Example of st.text_input")

name = st.text_input(label='What is your name', 
                      value="",
                      help="hit enter after typing compeleted",
                      max_chars=100,
                      type='default',
                      autocomplete='on',
                      placeholder='type your name'
                      )

st.write('My name is', name)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.text_input")

name = st.text_input(label='What is your name', 
                      value="",
                      help="hit enter after typing compeleted",
                      max_chars=100,
                      type='default',
                      autocomplete='on',
                      placeholder='type your name'
                      )

st.write('My name is', name)
"""
my_code(code_example)
st.divider()