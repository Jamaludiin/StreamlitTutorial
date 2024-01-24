import streamlit as st

if 'count' not in st.session_state:
    st.session_state.count = 0

if 'quotes' not in st.session_state:
    st.session_state.quotes = [
        "http://localhost:8501/home",
        "http://localhost:8501/L1",
        "http://localhost:8501/L2",
        "http://localhost:8501/L3",
        "http://localhost:8501/L4"
    ]

def display_quote():
    quote = st.session_state.quotes[st.session_state.count]
    st.write(quote)

def next_quote():
    if st.session_state.count + 1 >= len(st.session_state.quotes):
        st.session_state.count = 0
    else:
        st.session_state.count += 1

def previous_quote():
    if st.session_state.count > 0:
        st.session_state.count -= 1



#---------------------------------------------
st.title("Inspirational Quotes")

display_quote()

col1, col2 = st.columns(2)

with col1:
    if st.button("⏮️ Previous", on_click=previous_quote):
        pass

with col2:
    if st.button("Next ⏭️", on_click=next_quote):
        pass