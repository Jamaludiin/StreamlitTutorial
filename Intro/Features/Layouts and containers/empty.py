import streamlit as st
import time


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.empty()

st.subheader("1: Example of st.empty")

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("The 10 seconds is over!")


st.subheader("This another example")

with st.empty():
    time.sleep(5)
st.success("Success message!")
st.warning("This is a warning message!")
st.error("Error happen! message")



#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import time

st.subheader("1: Example of st.empty")

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("The 10 seconds is over!")


st.subheader("This another example")

with st.empty():
    time.sleep(5)
st.success("Success message!")
st.warning("This is a warning message!")
st.error("Error happen! message")

"""
my_code(code_example)
st.divider()