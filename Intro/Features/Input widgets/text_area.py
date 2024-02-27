import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.text_area")

st.text_area(label="Put your text Notes in here", height=200, max_chars=2000, placeholder="My plan in this week is good enough",label_visibility="visible")

st.write("This is another text area with hidden labe visiblity")


st.text_area(label="Write some text in here", 
             height=100, 
             max_chars=1500, 
             placeholder="In literary theory, a text is any object that can be read, whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some",
             label_visibility="visible")
