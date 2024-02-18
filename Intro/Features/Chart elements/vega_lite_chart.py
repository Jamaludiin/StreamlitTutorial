import streamlit as st
import pandas as pd
from vega_datasets import data

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.vega_lite_chart(data=None, spec=None, use_container_width=False, theme="streamlit", **kwargs)
st.subheader("1: Example of st.vega_lite_chart")

# Data representing student scores across different subjects
student_scores = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
    "Mathematics": [90, 85, 92, 88, 94, 90],
    "Science": [85, 88, 90, 86, 89, 87],
    "English": [88, 90, 87, 85, 91, 89],
    "History": [84, 86, 88, 83, 87, 85],
    "Geography": [82, 84, 86, 80, 85, 83]
}
chart_data = pd.DataFrame(student_scores)

st.vega_lite_chart(
   chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "Science", "type": "quantitative"},
           "y": {"field": "Mathematics", "type": "quantitative"},
           "size": {"field": "Geography", "type": "quantitative"},
           "color": {"field": "Geography", "type": "quantitative"},
       },
   },
   use_container_width=True, theme="streamlit"
)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("1: Example of st.vega_lite_chart")

# Data representing student scores across different subjects
student_scores = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
    "Mathematics": [90, 85, 92, 88, 94, 90],
    "Science": [85, 88, 90, 86, 89, 87],
    "English": [88, 90, 87, 85, 91, 89],
    "History": [84, 86, 88, 83, 87, 85],
    "Geography": [82, 84, 86, 80, 85, 83]
}
chart_data = pd.DataFrame(student_scores)

st.vega_lite_chart(
   chart_data,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "Science", "type": "quantitative"},
           "y": {"field": "Mathematics", "type": "quantitative"},
           "size": {"field": "Geography", "type": "quantitative"},
           "color": {"field": "Geography", "type": "quantitative"},
       },
   },
   use_container_width=True, theme="streamlit"
)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.vega_lite_chart(data=None, spec=None, use_container_width=False, theme="streamlit", **kwargs)
st.subheader("2: Example of st.vega_lite_chart")

source = data.cars()

st.dataframe(source,width=700)

chart_data = pd.DataFrame(source)

st.vega_lite_chart(
   source,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "Miles_per_Gallon", "type": "quantitative"},
           "y": {"field": "Cylinders", "type": "quantitative"},
           "size": {"field": "Displacement", "type": "quantitative"},
           "color": {"field": "Displacement", "type": "quantitative"},
       },
   },
   use_container_width=True, theme="streamlit"
)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
from vega_datasets import data

st.subheader("2: Example of st.vega_lite_chart")

source = data.cars()

st.dataframe(source,width=700)

chart_data = pd.DataFrame(source)

st.vega_lite_chart(
   source,
   {
       "mark": {"type": "circle", "tooltip": True},
       "encoding": {
           "x": {"field": "Miles_per_Gallon", "type": "quantitative"},
           "y": {"field": "Cylinders", "type": "quantitative"},
           "size": {"field": "Displacement", "type": "quantitative"},
           "color": {"field": "Displacement", "type": "quantitative"},
       },
   },
   use_container_width=True, theme="streamlit"
)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.vega_lite_chart(data=None, spec=None, use_container_width=False, theme="streamlit", **kwargs)
st.subheader("3: Example of st.vega_lite_chart")

# this code is from streamlit website https://docs.streamlit.io/library/api-reference/charts/st.vega_lite_chart

source = data.cars()

chart = {
    "mark": "point",
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},
        "shape": {"field": "Origin", "type": "nominal"},
    },
}

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.vega_lite_chart(
        source, chart, theme="streamlit", use_container_width=True
    )
with tab2:
    st.vega_lite_chart(
        source, chart, theme=None, use_container_width=True
    )