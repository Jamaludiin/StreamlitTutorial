import streamlit as st
import pandas as pd

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
st.subheader("1: Example of st.download_button")

st.write("Downloading a string or text as a file")

prmt_download = '''Download this prompt: Hi GPT4 I am comming to Overtake your role'''
st.download_button('Download some text', prmt_download,disabled=True,use_container_width=True,type="primary")
# this will put the text to .txt file and saves to the download folder 

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.download_button")

st.write("Downloading a string or text as a file")

prmt_download = '''Download this prompt: Hi GPT4 I am comming to Overtake your role'''
st.download_button('Download some text', prmt_download,disabled=True,use_container_width=True,type="primary")
# this will put the text to .txt file and saves to the download folder 
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
st.subheader("2: Example of st.download_button")

# Assuming my_large_df is a DataFrame you have created or loaded from somewhere
var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
my_large_df = pd.DataFrame(var_dic_data_1)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Scores_file.csv',
    mime='text/csv',
)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example of st.download_button")

# Assuming my_large_df is a DataFrame you have created or loaded from somewhere
var_dic_data_1 = {
    "Score 1": [90,33,55,66,88,99], 
    "Score 2": [100,99,88,55,77,56],
    "Score 3": [93,44,89,56,87,43],
    "Score 4": [84,45,76,63,83,82],
    "Score 5": [55,12,76,84,75,79]
}
my_large_df = pd.DataFrame(var_dic_data_1)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Scores_file.csv',
    mime='text/csv',
)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
st.subheader("3: Example of st.download_button")

binary_contents = b'Binary file example of st.download_button'

st.download_button('Download binary file', binary_contents,file_name="Binary_file")

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.download_button")

binary_contents = b'Binary file example of st.download_button'

st.download_button('Download binary file', binary_contents,file_name="Binary_file")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
st.subheader("4: Example of st.download_button")

with open("streamlit-mark-color.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="streamlit-mark-color.png",
            mime="image/png"
          )

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
st.subheader("4: Example of st.download_button")

with open("streamlit-mark-color.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="streamlit-mark-color.png",
            mime="image/png"
          )
"""
my_code(code_example)
st.divider()