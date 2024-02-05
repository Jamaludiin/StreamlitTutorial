import streamlit as st
import pandas as pd
from numpy import random

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

#_____________________________________________________________
st.title("5: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd


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
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
st.title("6: Example of outofilling some text areas with row values)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

# Display the DataFrame with data editor
edited_df = st.data_editor(df)

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox")

# Text boxes to display row data
if fill_checkbox:
    selected_row_index = edited_df[edited_df["Fill"] == True].index[0]  # Index of the first row where "Fill" is True
    selected_row = df.iloc[selected_row_index]
    st.text_input("Name", selected_row["Name"], key="textbox1")
    st.text_input("Score", str(selected_row["Score"]), key="textbox2")
    st.text_input("Pass", str(selected_row["Pass"]), key="textbox3")
    st.text_input("Gift", selected_row["Gift"], key="textbox4")
else:
    st.text_input("Name", "", key="textbox1")
    st.text_input("Score", "", key="textbox2")
    st.text_input("Pass", "", key="textbox3")
    st.text_input("Gift", "", key="textbox4")
#_____________________________________________________________
st.title("6: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

# Display the DataFrame with data editor
edited_df = st.data_editor(df)

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox")

# Text boxes to display row data
if fill_checkbox:
    selected_row_index = edited_df[edited_df["Fill"] == True].index[0]  # Index of the first row where "Fill" is True
    selected_row = df.iloc[selected_row_index]
    st.text_input("Name", selected_row["Name"], key="textbox1")
    st.text_input("Score", str(selected_row["Score"]), key="textbox2")
    st.text_input("Pass", str(selected_row["Pass"]), key="textbox3")
    st.text_input("Gift", selected_row["Gift"], key="textbox4")
else:
    st.text_input("Name", "", key="textbox1")
    st.text_input("Score", "", key="textbox2")
    st.text_input("Pass", "", key="textbox3")
    st.text_input("Gift", "", key="textbox4")
"""
my_code(code_example)
st.divider()

# -------------------------------------------------------------------------------------
st.title("7: Example of autofilling some text areas with row values with another way)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with no error if all fill disalected")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox1")
# Text boxes to display row data
if fill_checkbox:
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        selected_row_index = edited_df[edited_df["Fill"] == True].index[0]  # Index of the first row where "Fill" is True
        selected_row = df.iloc[selected_row_index]
        st.text_input("Name", selected_row["Name"], key="textbox10")
        st.text_input("Score", str(selected_row["Score"]), key="textbox20")
        st.text_input("Pass", str(selected_row["Pass"]), key="textbox30")
        st.text_input("Gift", selected_row["Gift"], key="textbox40")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key="textbox10")
    st.text_input("Score", "", key="textbox20")
    st.text_input("Pass", "", key="textbox30")
    st.text_input("Gift", "", key="textbox40")

#_____________________________________________________________
st.title("7: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with no error if all fill disalected")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox1")
# Text boxes to display row data
if fill_checkbox:
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        selected_row_index = edited_df[edited_df["Fill"] == True].index[0]  # Index of the first row where "Fill" is True
        selected_row = df.iloc[selected_row_index]
        st.text_input("Name", selected_row["Name"], key="textbox10")
        st.text_input("Score", str(selected_row["Score"]), key="textbox20")
        st.text_input("Pass", str(selected_row["Pass"]), key="textbox30")
        st.text_input("Gift", selected_row["Gift"], key="textbox40")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key="textbox10")
    st.text_input("Score", "", key="textbox20")
    st.text_input("Pass", "", key="textbox30")
    st.text_input("Gift", "", key="textbox40")
"""
my_code(code_example)
st.divider()


# -------------------------------------------------------------------------------------
st.title("8: Example of outo fill and auto key widget generation with for loop)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with outo fill and auto key widget generation with for loop")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor1")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox2")
# Text boxes to display row data
if fill_checkbox:
    i = 0
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        for index, row in edited_df.iterrows():
            st.subheader(f"The row {index} included this record")
            st.text_input("Name", row["Name"], key=f"{str(index)+'text1'}")
            st.text_input("Score", str(row["Score"]), key=f"{str(index)+'text2'}")
            st.text_input("Pass", str(row["Pass"]), key=f"{str(index)+'text3'}")
            st.text_input("Gift", row["Gift"], key=f"{str(index)+'text4'}")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key=f"{str(index)+'text1'}")
    st.text_input("Score", "", key=f"{str(index)+'text2'}")
    st.text_input("Pass", "", key=f"{str(index)+'text3'}")
    st.text_input("Gift", "", key=f"{str(index)+'text4'}")

#_____________________________________________________________
st.title("8: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with outo fill and auto key widget generation with for loop")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor1")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key="fill_checkbox2")
# Text boxes to display row data
if fill_checkbox:
    i = 0
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        for index, row in edited_df.iterrows():
            st.subheader(f"The row {index} included this record")
            st.text_input("Name", row["Name"], key=f"{str(index)+'text1'}")
            st.text_input("Score", str(row["Score"]), key=f"{str(index)+'text2'}")
            st.text_input("Pass", str(row["Pass"]), key=f"{str(index)+'text3'}")
            st.text_input("Gift", row["Gift"], key=f"{str(index)+'text4'}")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key=f"{str(index)+'text1'}")
    st.text_input("Score", "", key=f"{str(index)+'text2'}")
    st.text_input("Pass", "", key=f"{str(index)+'text3'}")
    st.text_input("Gift", "", key=f"{str(index)+'text4'}")
"""
my_code(code_example)
st.divider()

# ---------------------------------------------------------
st.title("9: Example of outo fill and auto key widget generation with for loop)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with outo fill and auto key widget generation with for loop")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="fill_checkbox3")

st.subheader("Select the values to be displayed by selecting the Fill column")
st.write(edited_df[edited_df["Fill"] == True])

#_____________________________________________________________
st.title("9: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np


# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way with outo fill and auto key widget generation with for loop")

# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="fill_checkbox3")
st.subheader("Select the values to be displayed by selecting the Fill column")
st.write(edited_df[edited_df["Fill"] == True])
"""
my_code(code_example)
st.divider()

# ---------------------------------------------------------
st.title("10: Example of auto fill and auto key widget generation with for loop)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way of auto filling and output will be the last selected row. auto key widget generation with for loop")
# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor4")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key=f"{str(index)+'chkbox2'}")
# Text boxes to display row data
if fill_checkbox:
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        selected_rows = edited_df[edited_df["Fill"] == True]  # Select all rows marked for filling
        last_selected_row_index = selected_rows.index[-1]  # Index of the last selected row
        last_selected_row = df.loc[last_selected_row_index]  # Retrieve the row data
        
        st.text_input("Name", last_selected_row["Name"], key=f"{str(index)+'text14'}")
        st.text_input("Score", str(last_selected_row["Score"]), key=f"{str(index)+'text24'}")
        st.text_input("Pass", str(last_selected_row["Pass"]), key=f"{str(index)+'text34'}")
        st.text_input("Gift", last_selected_row["Gift"], key=f"{str(index)+'text44'}")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key=f"{str(index)+'text14'}")
    st.text_input("Score", "", key=f"{str(index)+'text24'}")
    st.text_input("Pass", "", key=f"{str(index)+'text34'}")
    st.text_input("Gift", "", key=f"{str(index)+'text44'}")

#_____________________________________________________________
st.title("10: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.write("Another way of auto filling and output will be the last selected row. auto key widget generation with for loop")
# Display the DataFrame with data editor
edited_df = st.data_editor(df, key="data_editor4")

# Checkbox to fill data
fill_checkbox = st.checkbox("Fill", key=f"{str(index)+'chkbox2'}")
# Text boxes to display row data
if fill_checkbox:
    if any(edited_df["Fill"]):  # Check if any row is marked for filling
        selected_rows = edited_df[edited_df["Fill"] == True]  # Select all rows marked for filling
        last_selected_row_index = selected_rows.index[-1]  # Index of the last selected row
        last_selected_row = df.loc[last_selected_row_index]  # Retrieve the row data
        
        st.text_input("Name", last_selected_row["Name"], key=f"{str(index)+'text14'}")
        st.text_input("Score", str(last_selected_row["Score"]), key=f"{str(index)+'text24'}")
        st.text_input("Pass", str(last_selected_row["Pass"]), key=f"{str(index)+'text34'}")
        st.text_input("Gift", last_selected_row["Gift"], key=f"{str(index)+'text44'}")
    else:
        st.text("No row selected for filling.")
else:
    st.text_input("Name", "", key=f"{str(index)+'text14'}")
    st.text_input("Score", "", key=f"{str(index)+'text24'}")
    st.text_input("Pass", "", key=f"{str(index)+'text34'}")
    st.text_input("Gift", "", key=f"{str(index)+'text44'}")
"""
my_code(code_example)
st.divider()


 # for index, row in edited_df.iterrows():
           # if row["Fill"]:
            #  st.write(row)

# Text boxes to display row data

#st.text_input("Name", edited_df.loc[edited_df["Gift"] == "$48", "Name"].values[0], key="textbox10")
#st.text_input("Score", edited_df.loc[edited_df["Gift"] == "$48", "Score"].values[0], key="textbox20")
#st.text_input("Pass", edited_df.loc[edited_df["Gift"] == "$48", "Pass"].values[0], key="textbox30")
#st.text_input("Gift", edited_df.loc[edited_df["Gift"] == "$48", "Gift"].values[0], key="textbox40")


# st.text_input("Name", edited_df.loc["Fill"] == True ["Name"], key="textbox8")

# st.text_input("Name", edited_df.loc[edited_df["Gift"] == "$48", "Name"].values[0], key="textbox8")

# Display the DataFrame
#edited_df = st.data_editor(df)
#the_selected_row = edited_df.loc[edited_df["Fill"]]
#st.subheader("The Selected info is")

# code to capture row clicks .ex. when the fill only becomes true
#if edited_df["Fill"] ==  True:
    #st.text_input("Name", edited_df.loc["Fill"] == True ["Name"], key="textbox1")
    #st.text_input("Score", edited_df["Score"], key="textbox2")
    #st.text_input("Pass", edited_df["Pass"], key="textbox3")
    #st.text_input("Gift", edited_df["Gift"], key="textbox4")
#else:
  # st.write("Not selected row fill")

# winder_name = edited_df.loc[edited_df["Score"].idxmax()]["Name"]
