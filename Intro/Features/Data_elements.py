# Data elements
import streamlit as st
import pandas as pd
import numpy as np

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("1: Example of st.dataframe element")

var_dic_data = {
    "Score 1": 90,
    "Score 2": 100,
    "Score 3": 93,
    "Score 4": 84,
    "Score 5": 55
}

var_series_data = pd.Series(var_dic_data)

st.dataframe(var_series_data, width=200, height=200)
st.subheader("The above output is series")

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

var_dic_data = {
    "Score 1": 90,
    "Score 2": 100,
    "Score 3": 93,
    "Score 4": 84,
    "Score 5": 55
}

var_series_data = pd.Series(var_dic_data)

st.dataframe(var_series_data, width=200, height=200)
st.subheader("The above output is series")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("2: Example of st.dataframe element")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_series_data_1 = pd.Series(var_dic_data_1)

st.dataframe(var_series_data_1)

st.subheader("The above output is dictionary converted to series")

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_series_data_1 = pd.Series(var_dic_data_1)

st.dataframe(var_series_data_1)

st.subheader("The above output is dictionary converted to series")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("3: Example of st.dataframe element")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_data_frame = pd.DataFrame(var_dic_data, index= (1,2,3,4,5))
             
st.dataframe(var_data_frame)

st.subheader("The above output is dictionary converted to DataFrame")

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_data_frame = pd.DataFrame(var_dic_data, index= (1,2,3,4,5))
             
st.dataframe(var_data_frame)

st.subheader("The above output is dictionary converted to DataFrame")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("4: Example of st.dataframe element")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_data_frame = pd.DataFrame(var_dic_data, index= (1,2,3,4,5))

st.subheader("indexing specific row in dataframe. so you cannot use the [index number] instead use the loc")
st.dataframe(var_data_frame.loc[1])

st.subheader("return row 1 and 2")
st.dataframe(var_data_frame.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.title("1: Example of st.dataframe element")

var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 4": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
var_data_frame = pd.DataFrame(var_dic_data, index= (1,2,3,4,5))

st.subheader("indexing specific row in dataframe. so you cannot use the [index number] instead use the loc")
st.dataframe(var_data_frame.loc[1])

st.subheader("return row 1 and 2")
st.dataframe(var_data_frame.loc[[1, 2]]) # Note: When using [], the result is a Pandas DataFrame.

"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("5: Example of st.dataframe element")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

st.dataframe(var_csv_data)

# The head() method returns the headers and a specified number of rows, starting from the top.
st.subheader("The first ten rows")
st.dataframe(var_csv_data.head(10))

# if you dont specify any parameter it will return the first five rows
st.subheader("The first five rows")
st.dataframe(var_csv_data.head())
#_____________________________________________________________
st.title("5: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

st.dataframe(var_csv_data) 

# The head() method returns the headers and a specified number of rows, starting from the top.
st.subheader("The first ten rows")
st.dataframe(var_csv_data.head(10))

# if you dont specify any parameter it will return the first five rows
st.subheader("The first five rows")
st.dataframe(var_csv_data.head())
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("6: Example of st.dataframe element")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

# There is also a tail() method for viewing the last rows of the DataFrame.
st.subheader("The last five rows")
st.dataframe(var_csv_data.tail())

st.subheader("The last ten rows")
st.dataframe(var_csv_data.tail(10))

#_____________________________________________________________
st.title("6: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

# There is also a tail() method for viewing the last rows of the DataFrame.
st.subheader("The last five rows")
st.dataframe(var_csv_data.tail())

st.subheader("The last ten rows")
st.dataframe(var_csv_data.tail(10))

"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("7: Example of st.dataframe element")

# Creating column names
columns = []
for i in range(20):
    columns.append("Random %d" % i)

# Creating a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(50, 20), columns=columns)

checkbox_1 = st.checkbox("Highlight the maximum value along each column ")
checkbox_2 = st.checkbox("Highlight the minimum value along each column ")

if checkbox_1:
    st.dataframe(df.style.highlight_max(axis=0))
elif checkbox_2:
    st.dataframe(df.style.highlight_min(axis=0))
elif checkbox_1 & checkbox_2 == False:
    st.dataframe(df)
#_____________________________________________________________
st.title("7: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np
# Creating column names
columns = []
for i in range(20):
    columns.append("col %d" % i)

# Creating a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(50, 20), columns=columns)


checkbox_1 = st.checkbox("Highlight the maximum value along each column ")
checkbox_2 = st.checkbox("Highlight the minimum value along each column ")

if checkbox_1:
    st.dataframe(df.style.highlight_max(axis=0))
elif checkbox_2:
    st.dataframe(df.style.highlight_min(axis=0))
elif checkbox_1 & checkbox_2 == False:
    st.dataframe(df)
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("8: Example of st.dataframe element")

# Creating column names
columns = []
for i in range(20):
    columns.append("Random %d" % i)

# Creating a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(50, 20), columns=columns)

highlight_option = st.radio("Select Highlighting Option", ["Maximum Value", "Minimum Value", "No Highlight"])


if highlight_option == "Maximum Value":
    st.dataframe(df.style.highlight_max(axis=0))
elif highlight_option == "Minimum Value":
    st.dataframe(df.style.highlight_min(axis=0))
elif highlight_option == "No Highlight":
    st.dataframe(df)
#_____________________________________________________________
st.title("8: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

# Creating column names
columns = []
for i in range(20):
    columns.append("Random %d" % i)

# Creating a DataFrame with random numbers
df = pd.DataFrame(np.random.randn(50, 20), columns=columns)

highlight_option = st.radio("Select Highlighting Option", ["Maximum Value", "Minimum Value", "No Highlight"])


if highlight_option == "Maximum Value":
    st.dataframe(df.style.highlight_max(axis=0))
elif highlight_option == "Minimum Value":
    st.dataframe(df.style.highlight_min(axis=0))
elif highlight_option == "No Highlight":
    st.dataframe(df)
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, 
# column_order=None, column_config=None)

st.title("9: Example of st.dataframe element")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

df = pd.DataFrame(var_csv_data)
st.write(df)

highlight_option = st.radio("Select Highlighting Option", ["Mean Value", "Median Value", "Mode Value"])

# Populate radio button with column names
selected_column = st.radio("Select Column Option", df.columns.tolist())
# Calculate statistics based on selected options
if highlight_option == "Mean Value":
    st.write("Mean Value of", selected_column, ":", df[selected_column].mean())
elif highlight_option == "Median Value":
    st.write("Median Value of", selected_column, ":", df[selected_column].median())
elif highlight_option == "Mode Value":
    st.write("Mode Value of", selected_column, ":", df[selected_column].mode())

#_____________________________________________________________
st.title("9: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np


var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

df = pd.DataFrame(var_csv_data)
st.write(df)

highlight_option = st.radio("Select Highlighting Option", ["Mean Value", "Median Value", "Mode Value"])

# Populate radio button with column names
selected_column = st.radio("Select Column Option", df.columns.tolist())

# Calculate statistics based on selected options
if highlight_option == "Mean Value":
    st.write("Mean Value of", selected_column, ":", df[selected_column].mean())
elif highlight_option == "Median Value":
    st.write("Median Value of", selected_column, ":", df[selected_column].median())
elif highlight_option == "Mode Value":
    st.write("Mode Value of", selected_column, ":", df[selected_column].mode())

"""
my_code(code_example)
st.divider()



















