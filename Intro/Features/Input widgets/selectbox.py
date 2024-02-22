import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.subheader("1: Example of st.selectbox")

payment_option = st.selectbox(
    'Select the payment option you want?',
    ["Master Card", "Online Banking", "Pay by Cash"])

st.write('You selected to pay through:', payment_option)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.selectbox")

payment_option = st.selectbox(
    'Select the payment option you want?',
    ["Master Card", "Online Banking", "Pay by Cash"])

st.write('You selected to pay through:', payment_option)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.subheader("2: Example of st.selectbox")

# Create a selectbox with all arguments and parameters
selected_option = st.selectbox(
    label="Choose an Option",
    options=["Option 1", "Option 2", "Option 4", "Option 5"],
    index=0,
    
    key="selectbox_key",
    help="Select one of the options",
    
    placeholder="Choose an option",
    disabled=False,
    label_visibility="visible"
)

st.write('You selected to pay through:', payment_option)
