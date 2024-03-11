import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.chat_input(placeholder="Your message", *, key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)

st.subheader("1: Example of st.chat_input")

Message = st.chat_input("Send a message")
if Message:
    st.write(f"User: {Message}")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.chat_input")

Message = st.chat_input("Send a message")
if Message:
    st.write(f"User: {Message}")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.chat_input(placeholder="Your message", *, key=None, max_chars=None, disabled=False, on_submit=None, args=None, kwargs=None)

st.subheader("2: Example of st.chat_input")

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Write a message"):
        messages.chat_message("user: ").write(prompt)
        messages.chat_message("assistant: ").write(f"Echo: {prompt}")

# or you can write like this
with st.sidebar:
    messages = st.container(height=400)
    if (prompt := st.chat_input("Write a messages")):
        messages.write("user : " + prompt)
        messages.write("assistant : " + f"Echo : {prompt}")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.chat_input")

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Write a message"):
        messages.chat_message("user: ").write(prompt)
        messages.chat_message("assistant: ").write(f"Echo: {prompt}")

# or you can write like this
with st.sidebar:
    messages = st.container(height=400)
    if (prompt := st.chat_input("Write a messages")):
        messages.write("user : " + prompt)
        messages.write("assistant : " + f"Echo : {prompt}")
"""
my_code(code_example)
st.divider()