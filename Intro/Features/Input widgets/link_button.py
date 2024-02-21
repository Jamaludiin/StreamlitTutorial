import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.link_button(label, url, *, help=None, type="secondary", disabled=False, use_container_width=False)
st.subheader("1: Example of st.link_button")

# Create a link button
btn1 = st.link_button("Go to transformers", "https://huggingface.co/docs/transformers/en/installation", use_container_width=True)

# Display different messages based on whether the button is clicked
if btn1:
    st.write("Wow you visited the Hugging Face Transformers installation Guide")
    visited = True
else:
    visited = False

# Display the state of the button
st.write("State of the BUTTON:", visited)
    

st.link_button("Go to Github", "https://github.com/Jamaludiin",disabled=False, type="primary", use_container_width=True)
