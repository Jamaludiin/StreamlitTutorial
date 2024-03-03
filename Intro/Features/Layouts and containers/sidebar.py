import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.sidebar.[element_name]
# "with" notation
#with st.sidebar:
   # st.[element_name]

st.subheader("1: Example of st.sidebar")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)


add_selectbox = st.sidebar.multiselect(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)

add_selectbox = st.sidebar.radio(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)

add_selectbox = st.sidebar.select_slider(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.sidebar")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)


add_selectbox = st.sidebar.multiselect(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)

add_selectbox = st.sidebar.radio(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)

add_selectbox = st.sidebar.select_slider(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.sidebar.[element_name]
# "with" notation
#with st.sidebar:
   # st.[element_name]

st.subheader("1: Example of st.sidebar 'with' notation")
# Using "with" notation
with st.sidebar:
    st.divider()
    st.subheader("st.sidebar 'with' notation")

    add_selectbox = st.sidebar.multiselect(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking"),
    key='multiselect1'
    )

    add_selectbox = st.sidebar.radio(
        "How would you like to pay your bills?",
        ("Card", "Cash", "Loan", "Online Banking"),
        key="radio1"
    )

    add_selectbox = st.sidebar.select_slider(
        "How would you like to pay your bills?",
        ("Card", "Cash", "Loan", "Online Banking"),
        key="select_slider"
    )