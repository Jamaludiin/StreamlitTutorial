import streamlit as st
import time
import pandas as pd

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.empty()

st.subheader("1: Example of st.empty")

with st.empty():
    for seconds in range(3):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("The 10 seconds is over!")


st.subheader("This another example")

with st.empty():
    time.sleep(5)
st.success("Success message!")
st.warning("This is a warning message!")
st.error("Error happen! message")



#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import time

st.subheader("1: Example of st.empty")

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("The 10 seconds is over!")


st.subheader("This another example")

with st.empty():
    time.sleep(5)
st.success("Success message!")
st.warning("This is a warning message!")
st.error("Error happen! message")

"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.empty()

st.subheader("2: Example of st.empty")

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("This is text with a single-element container called empty")


placeholder1 = st.empty()

# Replace the text with a chart:
placeholder1.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder1.container(border=True):
    st.write("This is text inside a container with empty object")

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

# Clear all those elements:
# placeholder.empty()


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example of st.empty")

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("This is text with a single-element container called empty")


placeholder1 = st.empty()

# Replace the text with a chart:
placeholder1.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder1.container(border=True):
    st.write("This is text inside a container with empty object")

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