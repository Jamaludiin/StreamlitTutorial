import streamlit as st
import pandas as pd


# Display a data editor widget.
# The data editor widget allows you to edit dataframes and many other data structures in a table-like UI.

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.data_editor(data, *, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, on_change=None, args=None, kwargs=None)
st.title("1: Example of st.data_editor element")

df = pd.DataFrame(
    [
       {"Name": "Leyla Haward", 
        "Score": 99, 
        "Pass": True,
        "Gift": "$200"
        },

       {"Name": "Mike Lepard", 
        "Score": 49, 
        "Pass": False,
        "Gift": "$50"
        },

       {"Name": "Joseph Coward", 
        "Score": 89, 
        "Pass": True,
        "Gift": "$270"
        },

        {"Name": "Munier Ali", 
        "Score": 43, 
        "Pass": False,
        "Gift": "$48"
        },
   ]
)

st.checkbox("Maximize the container width", value=True, key="use_container_width")

edited_df = st.data_editor(df,use_container_width=st.session_state.use_container_width)

st.subheader("The above output is Dataframe using data_editor")

# Display rows where "Pass" is True
st.subheader("Select the Pass Rows To display:")
for index, row in edited_df.iterrows():
    if row["Pass"]:
        st.write(row)
#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

# st.data_editor(data, *, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, on_change=None, args=None, kwargs=None)
st.title("1: Example of st.data_editor element")

df = pd.DataFrame(
    [
       {"Name": "Leyla Haward", 
        "Score": 99, 
        "Pass": True,
        "Gift": "$200"
        },

       {"Name": "Mike Lepard", 
        "Score": 49, 
        "Pass": False,
        "Gift": "$50"
        },

       {"Name": "Joseph Coward", 
        "Score": 89, 
        "Pass": True,
        "Gift": "$270"
        },

        {"Name": "Munier Ali", 
        "Score": 43, 
        "Pass": False,
        "Gift": "$48"
        },
   ]
)

st.checkbox("Maximize the container width", value=True, key="use_container_width")

edited_df = st.data_editor(df,use_container_width=st.session_state.use_container_width)

st.subheader("The above output is Dataframe using data_editor")

# Display rows where "Pass" is True
st.subheader("Select the Pass Rows To display:")
for index, row in edited_df.iterrows():
    if row["Pass"]:
        st.write(row)
"""

my_code(code_example)
st.divider()