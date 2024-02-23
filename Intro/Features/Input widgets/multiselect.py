import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, max_selections=None, placeholder="Choose an option", disabled=False, label_visibility="visible")

st.subheader("1: Example of st.multiselect")

selected_option= st.multiselect(label="Select the payment method",
               options=["Master Card", "Online Banking", "Pay by Cash"],
               placeholder="Choose an option",
               max_selections=None,

               disabled=False,
               label_visibility="visible"
)


st.write('You selected to pay through:', selected_option)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.multiselect")

selected_option= st.multiselect(label="Select the payment method",
               options=["Master Card", "Online Banking", "Pay by Cash"],
               placeholder="Choose an option",
               max_selections=None,

               disabled=False,
               label_visibility="visible"
)


st.write('You selected to pay through:', selected_option)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
st.subheader("2: Example of st.multiselect")

selected_option= st.multiselect(label="Select the payment method",
               options=["Master Card", "Online Banking", "Pay by Cash"],
               placeholder="Choose an option",
               max_selections=2,

               disabled=False,
               label_visibility="visible"
)


st.write('You selected to pay through:', selected_option)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.multiselect")

selected_option= st.multiselect(label="Select the payment method",
               options=["Master Card", "Online Banking", "Pay by Cash"],
               placeholder="Choose an option",
               max_selections=2,

               disabled=False,
               label_visibility="visible"
)


st.write('You selected to pay through:', selected_option)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 