import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.toggle(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("1: Example of st.toggle")

pypl = st.toggle("Select Payment Plan")

if pypl:
    st.write("You have selected Payment Plan Option")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.toggle")

pypl = st.toggle("Select Payment Plan")

if pypl:
    st.write("You have selected Payment Plan Option")

"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.toggle(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("2: Example of st.toggle")

pypl1 = st.toggle("Select Payment Plan",value=True)
pypl2 = st.toggle("Select non Payment Plan",value=False)


if pypl1:
    st.write("You have selected Payment Plan Option")

elif pypl2:
    st.write("You have selected Non Payment Plan Option")



#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("2: Example of st.toggle")

pypl1 = st.toggle("Select Payment Plan",value=True)
pypl2 = st.toggle("Select non Payment Plan",value=False)


if pypl1:
    st.write("You have selected Payment Plan Option")

elif pypl2:
    st.write("You have selected Non Payment Plan Option")
"""
my_code(code_example)
st.divider()