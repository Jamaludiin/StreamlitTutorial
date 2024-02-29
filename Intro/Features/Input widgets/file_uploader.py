import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a CSV file", type='csv', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("The File Name:", uploaded_file.name)
    st.write("The content and metadata retrieved:",bytes_data)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a CSV file", type='csv', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("The File Name:", uploaded_file.name)
    st.write("The content and metadata retrieved:",bytes_data)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("2: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a TXT file", type='txt', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("The File Name:", uploaded_file.name)
    st.write("The content and metadata retrieved:",bytes_data)


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a TXT file", type='txt', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("The File Name:", uploaded_file.name)
    st.write("The content and metadata retrieved:",bytes_data)
"""
my_code(code_example)
st.divider()


st.subheader("3: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a PYTHON file", type='py', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    # Decode bytes data into a string
    decoded_data = bytes_data.decode('utf-8')
    
    st.write("The File Name:", uploaded_file.name)
    #st.write("The content and metadata retrieved:", decoded_data)
    # Display clean code inside st.code()
    st.code(decoded_data)


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.file_uploader")

uploaded_files = st.file_uploader("Choose a PYTHON file", type='py', accept_multiple_files=True)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    # Decode bytes data into a string
    decoded_data = bytes_data.decode('utf-8')
    
    st.write("The File Name:", uploaded_file.name)
    #st.write("The content and metadata retrieved:", decoded_data)
    # Display clean code inside st.code()
    st.code(decoded_data)
"""
my_code(code_example)
st.divider()