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
    options=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
    index=0,
    
    key="selectbox_key",
    help="Select one of the options",
    
    placeholder="Choose an option",
    disabled=False,
    label_visibility="visible"
)

st.write('You selected to pay through:', selected_option)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.selectbox")

# Create a selectbox with all arguments and parameters
selected_option = st.selectbox(
    label="Choose an Option",
    options=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"],
    index=0,
    
    key="selectbox_key",
    help="Select one of the options",
    
    placeholder="Choose an option",
    disabled=False,
    label_visibility="visible"
)

st.write('You selected to pay through:', selected_option)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.subheader("3: Example of st.selectbox")

option_zero = "Not selected any plan yet"

option = st.selectbox(
   'Select the payment option you want?',
    ["Master Card", "Online Banking", "Pay by Cash"],
   index=None,
   placeholder="Select the payment plans....",
)

if option is None:
 st.write('You selected to pay through:', option_zero)
else:
 st.write('You selected to pay through:', option)
   
#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.selectbox")

option_zero = "Not selected any plan yet"

option = st.selectbox(
   'Select the payment option you want?',
    ["Master Card", "Online Banking", "Pay by Cash"],
   index=None,
   placeholder="Select the payment plans....",
)

if option is None:
 st.write('You selected to pay through:', option_zero)
else:
 st.write('You selected to pay through:', option)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")
st.subheader("4: Example of st.selectbox")

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
st.subheader("4: Example of st.selectbox")
# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

"""
my_code(code_example)
st.divider()