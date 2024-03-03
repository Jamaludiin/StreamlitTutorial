import streamlit as st
import numpy as np
import pandas as pd


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.container(*, height=None, border=None)

st.subheader("1: Example of st.container")

with st.container(border=2):
   st.write("This is inside the container using st.container")

   var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
     }
   area_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

   st.dataframe(area_chart,hide_index=False,width=700)

   st.subheader("Dont Specify only three columns")
   st.area_chart(area_chart, color=["#fd0", "#f0f", "#04f"])

   st.bar_chart(np.random.randn(50, 3))

# outside the container
st.subheader("This is outside the container box")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import numpy as np
import pandas as pd

st.subheader("1: Example of st.container")

with st.container(border=2):
   st.write("This is inside the container using st.container")

   var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
     }
   area_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

   st.dataframe(area_chart,hide_index=False,width=700)

   st.subheader("Dont Specify only three columns")
   st.area_chart(area_chart, color=["#fd0", "#f0f", "#04f"])

   st.bar_chart(np.random.randn(50, 3))

# outside the container
st.subheader("This is outside the container box")

"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.container(*, height=None, border=None)

st.subheader("2: Example of st.container with border True")

container = st.container(border=True)
container.header("The Program 2")
container.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png")

container.write("This is inside the container")

# outside the container
st.subheader("This is outside the container box")

# Now insert some more in the container
container.write("This is inside too")


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.container with border True")

container = st.container(border=True)
container.header("The Program 2")
container.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Sets.png")

container.write("This is inside the container")

# outside the container
st.subheader("This is outside the container box")

# Now insert some more in the container
container.write("This is inside too")
"""
my_code(code_example)
st.divider()