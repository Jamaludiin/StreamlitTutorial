import streamlit as st
import pandas as pd


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.expander(label, expanded=False)

st.subheader("1: Example of st.expander")


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write(
        """The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.""")
    st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Tuples.png")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("1: Example of st.expander")


st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write(
        "The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're *guaranteed* to be random.")
    st.image("/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/Python Tuples.png")

"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.expander(label, expanded=False)

st.subheader("2: Example of st.expander")
with st.expander("See More data and figures"):
    # display data
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
# expanded=False

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example of st.expander")
with st.expander("See More data and figures"):
    # display data
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
"""
my_code(code_example)
st.divider()