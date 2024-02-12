import streamlit as st
import pandas as pd
import numpy as np


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.table(data=None)
st.subheader("1: Example of st.table")

st.subheader("Dictionary data displayed in st.table")

var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

st.table(var_dictionaries)

st.subheader("Dictionary data converted to pd.series and displayed in st.table")
dataseries = pd.Series(var_dictionaries)
st.table(dataseries)


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("Dictionary data displayed in st.table")

var_dictionaries = {
                        "name": "Jamal",
                        "race": "Somali",
                        "weight": 78.80,
                        "student": True,
                        "age": 38,
                        "foodlist": ["Rice","Fish","Burger","Fried eggs"],
                        "carlist": {"Toyoto","Mercedes","BMW","Honda","Volvo"}
                   }

st.table(var_dictionaries)

st.subheader("Dictionary data converted to pd.series and displayed in st.table")
dataseries = pd.Series(var_dictionaries)
st.table(dataseries)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.table(data=None)
st.subheader("2: Example of st.table")

data = np.random.randn(10, 5)

# Create column names
column_names = []
for i in range(5):
    column_names.append("col {}".format(i))

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)
st.table(df)


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

st.subheader("2: Example of st.table")

data = np.random.randn(10, 5)

# Create column names
column_names = []
for i in range(5):
    column_names.append("col {}".format(i))

# Create DataFrame
df = pd.DataFrame(data, columns=column_names)
st.table(df)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.table(data=None)
st.subheader("3: Example of st.table with pd.DataFrame")
data_df = pd.DataFrame(
    {
     "Main Score": [
            [55,12,76,84,75,79],
            [84,45,76,63,83,82],
            [93,44,89,56,87,43],
            [100,99,88,55,77,56],
            [90,33,55,66,88,99], 
        ],

   "Score 2": [
               [90,33,55,66,88,99], 
               [84,45,76,63,83,82],
               [93,44,89,56,87,43],
               [100,99,88,55,77,56],
               [90,33,55,66,88,99],
               ],

    "Score 3": [[100,99,88,55,77,56],
                [93,44,89,56,87,43],
                [100,99,88,55,77,56],
                [90,33,55,66,88,99],
                [100,99,88,55,77,56],
                ]
    }
)


st.table(data_df)


# Transpose the DataFrame
st.subheader("2: Example of st.table with transposeed pd.DataFrame data")

progress_df_transposed = data_df.transpose()
st.table(progress_df_transposed)


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("3: Example of st.table with pd.DataFrame")
data_df = pd.DataFrame(
    {
     "Main Score": [
            [55,12,76,84,75,79],
            [84,45,76,63,83,82],
            [93,44,89,56,87,43],
            [100,99,88,55,77,56],
            [90,33,55,66,88,99], 
        ],

   "Score 2": [
               [90,33,55,66,88,99], 
               [84,45,76,63,83,82],
               [93,44,89,56,87,43],
               [100,99,88,55,77,56],
               [90,33,55,66,88,99],
               ],

    "Score 3": [[100,99,88,55,77,56],
                [93,44,89,56,87,43],
                [100,99,88,55,77,56],
                [90,33,55,66,88,99],
                [100,99,88,55,77,56],
                ]
    }
)


st.table(data_df)


# Transpose the DataFrame
st.subheader("2: Example of st.table with transposeed pd.DataFrame data")

progress_df_transposed = data_df.transpose()
st.table(progress_df_transposed)

"""
my_code(code_example)
st.divider()