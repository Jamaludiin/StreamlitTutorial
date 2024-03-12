import streamlit as st
import time
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.status(label, *, expanded=False, state="running")

st.subheader("1: Example of st.status")


with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun')


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import time
import numpy as np

st.subheader("1: Example of st.status")

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun')
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.status(label, *, expanded=False, state="running")

st.subheader("2: Example of st.status")

with st.status("Sending Message...", expanded=True):
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.write("My Friend 👋")
        st.line_chart(np.random.randn(30, 3))

    Message = st.chat_input("Send a message")
    if Message:
        st.write(f"User: {Message}")

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import numpy as np

st.subheader("2: Example of st.status")

with st.status("Sending Message...", expanded=True):
    with st.chat_message("user"):
        st.write("Hello 👋")
        st.write("My Friend 👋")
        st.line_chart(np.random.randn(30, 3))

    Message = st.chat_input("Send a message")
    if Message:
        st.write(f"User: {Message}")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.status(label, *, expanded=False, state="running")

st.subheader("3: Example of st.status")

with st.status("Sending Message...", expanded=True) as status:
    with st.chat_message("user"):
        time.sleep(1)
        st.write("Hello 👋")
        time.sleep(1)
        st.write("My Friend 👋")
        time.sleep(1)
        st.line_chart(np.random.randn(30, 3))

    Message = st.chat_input("Send a message..")
    if Message:
        st.write(f"User: {Message}")
        time.sleep(1)
    status.update(label="Message Sent!", state="complete", expanded=True)

st.button('Rerun again')


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import time
import numpy as np

st.subheader("3: Example of st.status")

with st.status("Sending Message...", expanded=True) as status:
    with st.chat_message("user"):
        time.sleep(1)
        st.write("Hello 👋")
        time.sleep(1)
        st.write("My Friend 👋")
        time.sleep(1)
        st.line_chart(np.random.randn(30, 3))

    Message = st.chat_input("Send a message..")
    if Message:
        st.write(f"User: {Message}")
        time.sleep(1)
    status.update(label="Message Sent!", state="complete", expanded=True)

st.button('Rerun again')
"""
my_code(code_example)
st.divider()