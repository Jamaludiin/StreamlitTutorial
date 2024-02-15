import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.bar_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)

st.subheader("1: Example of st.bar_chart")


var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

bar_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(bar_chart,hide_index=False,width=700)

st.subheader("Dont Specify any column names")
st.bar_chart(bar_chart)

# draw specific columns
st.subheader("Using the X and Y axis as the column names")
st.bar_chart(bar_chart, x="Score 1",y="Score 2",color="#ffaa00")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd


st.subheader("1: Example of st.bar_chart")


var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

bar_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(bar_chart,hide_index=False,width=700)

st.subheader("Dont Specify any column names")
st.bar_chart(bar_chart)

# draw specific columns
st.subheader("Using the X and Y axis as the column names")
st.bar_chart(bar_chart, x="Score 1",y="Score 2",color="#ffaa00")
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.area_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)

st.subheader("2: Example of st.area_chart")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

bar_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

st.dataframe(bar_chart,hide_index=False,width=700)

st.subheader("Dont Specify only three columns")
st.bar_chart(bar_chart, color=["#fd0", "#f0f", "#04f"])

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example of st.area_chart")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

bar_chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6), columns=["Score 1", "Score 2", "Score 3"])

st.dataframe(bar_chart,hide_index=False,width=700)

st.subheader("Dont Specify only three columns")
st.bar_chart(bar_chart, color=["#fd0", "#f0f", "#04f"])
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.area_chart(data=None, *, x=None, y=None, color=None, width=0, height=0, use_container_width=True)

st.subheader("3: Example of st.area_chart. Scores generated randomly")

chart_data = pd.DataFrame(
   {
       "Score 1": np.random.randn(50),
       "Score 2": np.random.randn(50),
       "Score 3": np.random.choice(["Week 1", "Week 2", "Week 3"], 50),
   }
)

st.bar_chart(chart_data, x="Score 1", y="Score 2", color="Score 3")

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

st.subheader("3: Example of st.area_chart. Scores generated randomly")

chart_data = pd.DataFrame(
   {
       "Score 1": np.random.randn(50),
       "Score 2": np.random.randn(50),
       "Score 3": np.random.choice(["Week 1", "Week 2", "Week 3"], 50),
   }
)

st.bar_chart(chart_data, x="Score 1", y="Score 2", color="Score 3")
"""
my_code(code_example)
st.divider()