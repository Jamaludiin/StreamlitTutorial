import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
st.subheader("1: Example of st.altair_chart using the Altair library")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(chart,hide_index=False,width=700)

chart = (
   alt.Chart(chart)
   .mark_circle()
   .encode(x="Score 1", y="Score 2", 
           size="Score 3", 
           color="Score 3", 
           tooltip=["Score 1", "Score 2", "Score 3", "Score 4", "Score 5"])
)

st.altair_chart(chart, use_container_width=True)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import altair as alt

st.subheader("1: Example of st.altair_chart using the Altair library")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}

chart = pd.DataFrame(var_dic_data_1, index= (1,2,3,4,5,6))

st.dataframe(chart,hide_index=False,width=700)

chart = (
   alt.Chart(chart)
   .mark_circle()
   .encode(x="Score 1", y="Score 2", 
           size="Score 3", 
           color="Score 3", 
           tooltip=["Score 1", "Score 2", "Score 3", "Score 4", "Score 5"])
)

st.altair_chart(chart, use_container_width=True)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
st.subheader("2: Example of st.altair_chart using the Altair library with meaninfull Data")

# Data representing student scores across different subjects
student_scores = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
    "Mathematics": [90, 85, 92, 88, 94, 90],
    "Science": [85, 88, 90, 86, 89, 87],
    "English": [88, 90, 87, 85, 91, 89],
    "History": [84, 86, 88, 83, 87, 85],
    "Geography": [82, 84, 86, 80, 85, 83]
}

# Create a DataFrame from the data
student_df = pd.DataFrame(student_scores)

# Display the DataFrame
st.dataframe(student_df, hide_index=False, width=700)

chart = (
   alt.Chart(student_df)
   .mark_circle()
   .encode(x="Semester", y="Mathematics", 
           size="Geography", 
           color="Geography", 
           tooltip=["Mathematics", "Science", "English", "History", "Geography"])
)

st.altair_chart(chart, use_container_width=True)



#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import altair as alt
  
st.subheader("2: Example of st.altair_chart using the Altair library with meaninfull Data")

# Data representing student scores across different subjects
student_scores = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
    "Mathematics": [90, 85, 92, 88, 94, 90],
    "Science": [85, 88, 90, 86, 89, 87],
    "English": [88, 90, 87, 85, 91, 89],
    "History": [84, 86, 88, 83, 87, 85],
    "Geography": [82, 84, 86, 80, 85, 83]
}

# Create a DataFrame from the data
student_df = pd.DataFrame(student_scores)

# Display the DataFrame
st.dataframe(student_df, hide_index=False, width=700)

chart = (
   alt.Chart(student_df)
   .mark_circle()
   .encode(x="Semester", y="Mathematics", 
           size="Geography", 
           color="Geography", 
           tooltip=["Mathematics", "Science", "English", "History", "Geography"])
)

st.altair_chart(chart, use_container_width=True)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
st.subheader("3: Example of st.altair_chart using the Altair library with real Data")

# to use the dataset of cars use this
# pip install vega_datasets
source = data.cars()

st.dataframe(source,width=700)

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Cylinders',
    color='Year',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)




# ---------------
source = data.cars()

st.dataframe(source,width=700)

chart = alt.Chart(source).mark_circle().encode(
    x='Miles_per_Gallon',
    y='Acceleration',
    color='Name',
).interactive()

tab3, tab4 = st.tabs(["Another Columns 1", "Another Columns 2"])

with tab3:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab4:

    chart = alt.Chart(source).mark_circle().encode(
        x='Weight_in_lbs',
        y='Cylinders',
        color='Acceleration',
    ).interactive()
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import altair as alt
from vega_datasets import data

st.subheader("3: Example of st.altair_chart using the Altair library with real Data")

# to use the dataset of cars use this
# pip install vega_datasets
source = data.cars()

st.dataframe(source,width=700)

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Cylinders',
    color='Year',
).interactive()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)




# ---------------
source = data.cars()

st.dataframe(source,width=700)

chart = alt.Chart(source).mark_circle().encode(
    x='Miles_per_Gallon',
    y='Acceleration',
    color='Name',
).interactive()

tab3, tab4 = st.tabs(["Another Columns 1", "Another Columns 2"])

with tab3:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab4:

    chart = alt.Chart(source).mark_circle().encode(
        x='Weight_in_lbs',
        y='Cylinders',
        color='Acceleration',
    ).interactive()
    # Use the native Altair theme.
    st.altair_chart(chart, theme=None, use_container_width=True)
"""
my_code(code_example)
st.divider()