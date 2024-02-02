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

the_maximum_scorer = edited_df.loc[edited_df["Score"].idxmax()]
st.subheader("The Highest Scorer is")
st.dataframe(the_maximum_scorer)

# return only the name of the person
winder_name = edited_df.loc[edited_df["Score"].idxmax()]["Name"]
st.markdown(f"The winner Name is **{winder_name}**")
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

the_maximum_scorer = edited_df.loc[edited_df["Score"].idxmax()]
st.subheader("The Highest Scorer is")
st.dataframe(the_maximum_scorer)

# return only the name of the person
winder_name = edited_df.loc[edited_df["Score"].idxmax()]["Name"]
st.markdown(f"The winner Name is **{winder_name}**")
"""

my_code(code_example)
st.divider()

#------------------------------------------------------------

st.title("2: Example of st.dataframe element, allow user to add and delete rows")
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

edited_df = st.data_editor(df,use_container_width=st.session_state.use_container_width, num_rows='dynamic')

st.subheader("The above output is allow user to delete and add using num_rows='dynamic'")

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.title("2: Example of st.dataframe element, allow user to add and delete rows")
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

edited_df = st.data_editor(df,use_container_width=st.session_state.use_container_width, num_rows='dynamic')

st.subheader("The above output is allow user to delete and add using num_rows='dynamic'")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------

# st.data_editor(data, *, width=None, height=None, use_container_width=False, 
# hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, 
# on_change=None, args=None, kwargs=None)

st.title("3: Example of Data Editor with Custom Settings using st.data_editor")

# Sample DataFrame
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

# Multiselect for selecting options
select_setting_option = st.selectbox("Select Option",['Hide Index','Fit Width 400','Column Order (Score Name Pass Gift)','Disable row edit'])

if select_setting_option == 'Hide Index':
    st.data_editor(df, hide_index=True)
elif select_setting_option == 'Fit Width 400':
    st.data_editor(df, use_container_width=400)
elif select_setting_option == 'Column Order (Score Name Pass Gift)':
    st.data_editor(df, column_order=('Score','Name','Pass','Gift'))
elif select_setting_option == 'Disable row edit':
    st.data_editor(df, num_rows='dynamic')

# Display data editor with selected settings
st.subheader("Data Editor with Custom Settings")

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.title("3: Example of Data Editor with Custom Settings using st.data_editor")

# Sample DataFrame
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

# Multiselect for selecting options
select_setting_option = st.selectbox("Select Option",['Hide Index','Fit Width 400','Column Order (Score Name Pass Gift)','Disable row edit'])

if select_setting_option == 'Hide Index':
    st.data_editor(df, hide_index=True)
elif select_setting_option == 'Fit Width 400':
    st.data_editor(df, use_container_width=400)
elif select_setting_option == 'Column Order (Score Name Pass Gift)':
    st.data_editor(df, column_order=('Score','Name','Pass','Gift'))
elif select_setting_option == 'Disable row edit':
    st.data_editor(df, num_rows='dynamic')

# Display data editor with selected settings
st.subheader("Data Editor with Custom Settings")
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------

# st.data_editor(data, *, width=None, height=None, use_container_width=False, 
# hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, 
# on_change=None, args=None, kwargs=None)

st.title("4: Example of Data Editor and Disabling some columns to edit using st.data_editor")

# Sample DataFrame
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

# Multiselect for selecting options
select_setting_option = st.multiselect("Select Columns not to be Edited",df.columns.tolist())

if select_setting_option:
    st.data_editor(df, disabled=(select_setting_option))
else:
    st.data_editor(df)

# Display data editor with selected settings
st.subheader(f"Data Editor with Custom Disable edit{select_setting_option}")

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.title("3: Example of Data Editor with Custom Settings using st.data_editor")

# Sample DataFrame
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

# Multiselect for selecting options
select_setting_option = st.multiselect("Select Columns not to be Edited",df.columns.tolist())

if select_setting_option:
    st.data_editor(df, disabled=(select_setting_option))
else:
    st.data_editor(df)

# Display data editor with selected settings
st.subheader(f"Data Editor with Custom Disable edit{select_setting_option}")
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------

# st.data_editor(data, *, width=None, height=None, use_container_width=False, 
# hide_index=None, column_order=None, column_config=None, num_rows="fixed", disabled=False, key=None, 
# on_change=None, args=None, kwargs=None)

st.title("5: Example of customizing the st.data_editor (column_config, hide_index, column_order, or disabled)")

# Sample DataFrame
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

edited_df = st.data_editor(
    df,
    column_config={
        "Name": "Student Names", # renamed the Name column
        "Score": st.column_config.NumberColumn(
            "Final Score", # renamed the Score column
            help="Maximum scores ranges from 0-100?",
            min_value=0,
            max_value=100,
            step=1,
            format="%d ⭐",
        ),
        "Pass": "Passed", # renamed the Pass column
    },
    disabled=["Name", "Pass"],
    hide_index=True,
)

# return only the name of the person
winder_name = edited_df.loc[edited_df["Score"].idxmax()]["Name"]
st.markdown(f"The winner Name is **{winder_name}**")