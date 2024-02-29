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