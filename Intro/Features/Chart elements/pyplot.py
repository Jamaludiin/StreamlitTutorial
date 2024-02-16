import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.pyplot(fig=None, clear_figure=None, use_container_width=True, **kwargs)

st.subheader("1: Example of st.line_chart")


var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

pyplot = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(pyplot,hide_index=False,width=700)

st.subheader("First pyplot using the Dictionary data converted to Dataframe")
fig, ax = plt.subplots()
ax.hist(pyplot, bins=20)

st.pyplot(fig)

#-------------------------
# Add some properties
st.subheader("Using the bins 5 and container False")
fig, ax = plt.subplots()
ax.hist(pyplot, bins=5)

st.pyplot(fig, use_container_width=False)

st.subheader("Using the bins 5 and container True")

st.pyplot(fig, use_container_width=True)

#------------------------

val = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(val, bins=25)

st.pyplot(fig)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.subheader("1: Example of st.line_chart")


var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

pyplot = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(pyplot,hide_index=False,width=700)

st.subheader("First pyplot using the Dictionary data converted to Dataframe")
fig, ax = plt.subplots()
ax.hist(pyplot, bins=20)

st.pyplot(fig)

#-------------------------
# Add some properties
st.subheader("Using the bins 5 and container False")
fig, ax = plt.subplots()
ax.hist(pyplot, bins=5)

st.pyplot(fig, use_container_width=False)

st.subheader("Using the bins 5 and container True")

st.pyplot(fig, use_container_width=True)

#------------------------

val = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(val, bins=25)

st.pyplot(fig)
"""
my_code(code_example)
st.divider()


