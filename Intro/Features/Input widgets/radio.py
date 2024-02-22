import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")

st.subheader("1: Example of st.radio")

pypl = st.radio(
"What's your favorite payment plan",
    [":rainbow[Master Card]", "***Online Banking***", "Pay by Cash :euro:"],
    captions = ["Save 20% percent.", "Get free drink", "Free gift card"])

if pypl == ':rainbow[Master Card]':
    st.write('You selected to pay through Master Card.:mastercard:')
elif pypl == "***Online Banking***":
    st.write("You selected to pay through Online Banking.:bank:")
elif pypl == "Pay by Cash :euro:":
    st.write("You selected to pay through Cash:dollar:")
else:
    st.write("You have not selected any Payment Plan Option")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.radio")

pypl = st.radio(
"What's your favorite payment plan",
    [":rainbow[Master Card]", "***Online Banking***", "Pay by Cash :euro:"],
    captions = ["Save 20% percent.", "Get free drink", "Free gift card"])

if pypl == ':rainbow[Master Card]':
    st.write('You selected to pay through Master Card.:mastercard:')
elif pypl == "***Online Banking***":
    st.write("You selected to pay through Online Banking.:bank:")
elif pypl == "Pay by Cash :euro:":
    st.write("You selected to pay through Cash:dollar:")
else:
    st.write("You have not selected any Payment Plan Option")

"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")

st.subheader("2: Example of st.radio")


# Create a radio button with all arguments and parameters
selected_index = st.radio(
    label="Choose an Option",
    options=["Option 1", "Option 2", "Option 3"],
    index=0,

    key="radio_key2",
    help="Select one of the options",

    disabled=False,
    horizontal=True,
    captions={"Option 1": "First Option", "Option 2": "Second Option", "Option 3": "Third Option"},
    label_visibility="visible"
)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.radio")

# Create a radio button with all arguments and parameters
selected_index = st.radio(
    label="Choose an Option",
    options=["Option 1", "Option 2", "Option 3"],
    index=0,

    key="radio_key2",
    help="Select one of the options",

    disabled=False,
    horizontal=True,
    captions={"Option 1": "First Option", "Option 2": "Second Option", "Option 3": "Third Option"},
    label_visibility="visible"
)

"""
my_code(code_example)
st.divider()