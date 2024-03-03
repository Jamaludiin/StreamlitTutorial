import streamlit as st
import numpy as np
import pandas as pd


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




#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
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

"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.tabs(tabs)

st.subheader("2: Example of st.tabs")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

#tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])


area_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

tab4.dataframe(area_chart,hide_index=False,width=700)

tab4.subheader("Dont Specify only three columns")
tab4.area_chart(area_chart, color=["#fd0", "#f0f", "#04f"])


data = np.random.randn(10, 1)

tab1.subheader("Dispalyed in Program 1 tab1")
tab1.line_chart(data)

tab2.subheader("Dispalyed in Program 2 tab2")
tab2.write(data)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import numpy as np
import pandas as pd

st.subheader("2: Example of st.tabs")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

#tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])


area_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

tab4.dataframe(area_chart,hide_index=False,width=700)

tab4.subheader("Dont Specify only three columns")
tab4.area_chart(area_chart, color=["#fd0", "#f0f", "#04f"])


data = np.random.randn(10, 1)

tab1.subheader("Dispalyed in Program 1 tab1")
tab1.line_chart(data)

tab2.subheader("Dispalyed in Program 2 tab2")
tab2.write(data)
"""
my_code(code_example)
st.divider()