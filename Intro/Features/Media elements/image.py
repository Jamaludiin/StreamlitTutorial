import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.subheader("1: Example of st.image")

st.image('Python Sets.png', caption='Python Sets cover page')

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.image")

st.image('Python Sets.png', caption='Python Sets cover page')
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
st.subheader("2: Example of st.image")

st.image('Python Tuples.png', 
         caption='Python Tuples cover page', 
         width=1000,
         use_column_width=False,
         clamp=True,
         output_format="PNG")


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.image")

st.image('Python Tuples.png', 
         caption='Python Tuples cover page', 
         width=1000,
         use_column_width=False,
         clamp=True,
         output_format="PNG")
"""
my_code(code_example)
st.divider()