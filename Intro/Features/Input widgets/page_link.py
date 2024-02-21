import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.page_link(page, *, label=None, icon=None, help=None, disabled=False, use_container_width=None)
st.subheader("1: Example of st.page_link")


st.page_link("My Main Page.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")


# THIS PROGRAM TRIGER AN ERROR SAYING 'AttributeError: module 'streamlit' has no attribute 'page_link''
#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.page_link")


st.page_link("My Main Page.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
"""
my_code(code_example)
st.divider()