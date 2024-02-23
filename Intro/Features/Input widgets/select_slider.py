import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.select_slider")

payment_plan = st.select_slider(
    label='Select payment plan',
    options=['Online Banking', 'Cash', 'Master Card', 'E-Wallet', 'Gift Card', 'Loan', 'Credit Card'])
st.write('My favorite payment plan is', payment_plan)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.select_slider")

payment_plan = st.select_slider(
    label='Select payment plan',
    options=['Online Banking', 'Cash', 'Master Card', 'E-Wallet', 'Gift Card', 'Loan', 'Credit Card'])
st.write('My favorite payment plan is', payment_plan)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
st.subheader("2: Example of st.select_slider")

payment_plan1, payment_plan2 = st.select_slider(
    label='Select a range of color wavelength',
    options=['Online Banking', 'Cash', 'Master Card', 'E-Wallet', 'Gift Card', 'Loan', 'Credit Card'],
    value=('E-Wallet', 'Credit Card'))

st.write('My favorite payment plan is between', payment_plan1, 'and', payment_plan2)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.select_slider")

payment_plan1, payment_plan2 = st.select_slider(
    label='Select a range of color wavelength',
    options=['Online Banking', 'Cash', 'Master Card', 'E-Wallet', 'Gift Card', 'Loan', 'Credit Card'],
    value=('E-Wallet', 'Credit Card'))

st.write('My favorite payment plan is between', payment_plan1, 'and', payment_plan2)
"""
my_code(code_example)
st.divider()