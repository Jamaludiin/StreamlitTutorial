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
)