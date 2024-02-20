import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

st.subheader("1: Example of st.button")

btn1 = st.button("Button one", type="primary")

if btn1:
    st.write('You clicked button one')
else:
    st.write('Click button one')
    
#-----------------------
if st.button('Button two'):
    st.write('You clicked button two')
else:
    st.write('Click button two')
