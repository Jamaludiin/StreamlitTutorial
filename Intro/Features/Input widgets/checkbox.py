import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("1: Example of st.checkbox")

ck1 = st.checkbox("Select One",label_visibility="visible")

ck2 = st.checkbox("Select Two",label_visibility="hidden")
ck3 = st.checkbox("Select Three",label_visibility="visible")
ck4 = st.checkbox("Select Four")


if ck1:
    st.write('You selected One!')
elif ck2:
    st.write('You selected Two!')
elif ck3:
    st.write('You selected Three!')
elif ck4:
    st.write('You selected Four!')
else:
    st.write('You Have not selected any!')



#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.checkbox")

ck1 = st.checkbox("Select One",label_visibility="visible")

ck2 = st.checkbox("Select Two",label_visibility="hidden")
ck3 = st.checkbox("Select Three",label_visibility="visible")
ck4 = st.checkbox("Select Four")


if ck1:
    st.write('You selected One!')
elif ck2:
    st.write('You selected Two!')
elif ck3:
    st.write('You selected Three!')
elif ck4:
    st.write('You selected Four!')
else:
    st.write('You Have not selected any!')
"""
my_code(code_example)
st.divider()