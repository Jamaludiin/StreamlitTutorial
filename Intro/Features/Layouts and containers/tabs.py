import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.tabs(tabs)

st.subheader("1: Example of st.tabs")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Program 1", "Program 2", "Program 3", "Program 4", "Program 5"])

with tab1:
   st.header("The Program 1")
   st.markdown("My prompt")
   st.divider()
   st.markdown("This Program offers you..................")

   add_selectbox = st.sidebar.selectbox(
    "How would you like to pay your bills?",
    ("Card", "Cash", "Loan", "Online Banking")
   )

with tab2:
   st.header("The Program 2")
   st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png")

with tab3:
   st.header("The Program 3")
   st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png")

with tab4:
   st.header("The Program 4")
   st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png", width=200)

with tab5:
   st.header("The Program 5")
   st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png", width=200)
