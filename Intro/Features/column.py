import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import date
from datetime import time


# def
def my_code(code):
    st.code(f"""{code}""")
#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")
st.title("1: Example of st.columns element")

st.subheader("Display and group elements under Columns")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
   st.title("This is a TITLE of COLUMN ONE")
   st.header("This is a HEADER")
   st.subheader("This is SUBHEADER")
   st.write("This is a WRITE")

with col2:
    st.title("This is a TITLE of COLUMN TWO")
    st.checkbox("This CheckBox")
    st.multiselect("This CheckBox",['A','B','C','D'])

with col3:
   st.title("This is a TITLE of COLUMN THREE")
   st.header("Another HEADER")
   st.button("Button")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st

st.subheader("Display and group elements under Columns")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
   st.title("This is a TITLE of COLUMN ONE")
   st.header("This is a HEADER")
   st.subheader("This is SUBHEADER")
   st.write("This is a WRITE")

with col2:
    st.title("This is a TITLE of COLUMN TWO")
    st.checkbox("This CheckBox")
    st.multiselect("This CheckBox",['A','B','C','D'])

with col3:
   st.title("This is a TITLE of COLUMN THREE")
   st.header("Another HEADER")
   st.button("Button")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")
st.subheader("2: Example: Display charts and other data elements under Columns")

col1, col2 = st.columns([3, 1])
data = np.random.randn(100, 5)

col1.subheader("Column one with a chart")
col1.line_chart(data)

col2.subheader("The row Data in clumn two")
col2.write(data)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("2: Example: Display charts and other data elements under Columns")

col1, col2 = st.columns([3, 1])
data = np.random.randn(100, 5)

col1.subheader("Column one with a chart")
col1.line_chart(data)

col2.subheader("The row Data in clumn two")
col2.write(data)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")

st.subheader("3: Example: Display charts and other data elements under Columns")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

col1, col2 = st.columns([3, 1])

col1.subheader("Column one with a chart")
col1.bar_chart(var_csv_data[var_csv_data.columns.to_list()])
# col1.bar_chart(var_csv_data) same to the above

col2.subheader("Clumn two with row Data")
col2.write(var_csv_data)

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("3: Example: Display charts and other data elements under Columns")

var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

col1, col2 = st.columns([3, 1])

col1.subheader("Column one with a chart")
col1.bar_chart(var_csv_data)

col2.subheader("Clumn two with row Data")
col2.write(var_csv_data)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.columns(spec, *, gap="small")
st.subheader("4: Example: Display charts and other data elements under Columns")
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

# Populate radio button with column names
selected_column = st.radio("Select Column Option", var_csv_data.columns.tolist())

col1, col2 = st.columns([3, 1])
# Calculate statistics based on selected options
if selected_column in selected_column:
    col1.subheader("Column one with a chart")
    col1.line_chart(var_csv_data[selected_column])

    col2.subheader("Clumn two with median")
    col2.write(var_csv_data[selected_column].median())
else:
    pass

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("4: Example: Display charts and other data elements under Columns")
var_csv_data = pd.read_csv('/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/data.csv')

# Populate radio button with column names
selected_column = st.radio("Select Column Option", var_csv_data.columns.tolist())

col1, col2 = st.columns([3, 1])
# Calculate statistics based on selected options
if selected_column in selected_column:
    col1.subheader("Column one with a chart")
    col1.line_chart(var_csv_data[selected_column])

    col2.subheader("Clumn two with median")
    col2.write(var_csv_data[selected_column].median())
else:
    pass
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.column_config.Column(label=None, *, width=None, help=None, disabled=None, required=None)
st.subheader("5: Example: Column config")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.data_editor(
    df,
    column_config={
        "Name": st.column_config.Column(
            "Student Names",
            help="Student Pass School",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)

#_____________________________________________________________
st.title("5: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("5: Example: Column config")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.data_editor(
    df,
    column_config={
        "Name": st.column_config.Column(
            "Student Names",
            help="Student Pass School",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.column_config.TextColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, max_chars=None, validate=None)
st.subheader("6: Example: st.column_config.TextColumn")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})


st.data_editor(
    df,
    column_config={
        "Name": st.column_config.TextColumn(
            "Student Names",
            help="Student Pass School",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
    num_rows="dynamic"

)
#_____________________________________________________________
st.title("6: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("6: Example: st.column_config.TextColumn")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})


st.data_editor(
    df,
    column_config={
        "Name": st.column_config.TextColumn(
            "Student Names",
            help="Student Pass School",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
    num_rows="dynamic"

)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.column_config.NumberColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, format=None, min_value=None, max_value=None, step=None)
st.subheader("7: Example: st.column_config.NumberColumn")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})


st.data_editor(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(
            "Marks (0-100)",
            help="The score of the student",
            min_value=0,
            max_value=100,
            step=1,
            format="$%d",
        ),

        "Gift": st.column_config.NumberColumn(
            "Gift (0-300)",
            help="The Gift of the student",
            min_value=0,
            max_value=300,
            step=1,
            format="$%d",
        )
    },
    hide_index=False,
)

#_____________________________________________________________
st.title("7: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("7: Example: st.column_config.NumberColumn")
# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})


st.data_editor(
    df,
    column_config={
        "Score": st.column_config.NumberColumn(
            "Marks (0-100)",
            help="The score of the student",
            min_value=0,
            max_value=100,
            step=1,
            format="$%d",
        ),

        "Gift": st.column_config.NumberColumn(
            "Gift (0-300)",
            help="The Gift of the student",
            min_value=0,
            max_value=300,
            step=1,
            format="$%d",
        )
    },
    hide_index=False,
)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.column_config.CheckboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None)
st.subheader("7: Example: st.column_config.CheckboxColumn")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.data_editor(
    df,
    column_config={
        "Pass": st.column_config.CheckboxColumn(
            "Student Pass or Not?",
            help="Select student Pass",
            default=False,
        )
    },
    disabled=["Fill"],
    hide_index=False,
)

#_____________________________________________________________
st.title("8: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("8: Example: st.column_config.CheckboxColumn")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Leyla Haward", "Mike Lepard", "Joseph Coward", "Munier Ali"],
    "Score": [99, 49, 89, 43],
    "Pass": [True, False, True, False],
    "Gift": ["$200", "$50", "$270", "$48"],
    "Fill": [True, False, False, False],
})

st.data_editor(
    df,
    column_config={
        "Pass": st.column_config.CheckboxColumn(
            "Student Pass or Not?",
            help="Select student Pass",
            default=False,
        )
    },
    disabled=["Fill"],
    hide_index=False,
)
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.column_config.SelectboxColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, options=None)
st.subheader("9: Example: st.column_config.SelectboxColumn")
df = pd.DataFrame(
    {
        "Software Subjects": [
            "📊 Software Design",
            "📈 Software Modeling",
            "🤖 Software Measurement",
            "📊 Requirement Engineering",
            "📊 Requirement Engineering",
        ],
    }
)

selected_subject = st.data_editor(
    df,
    column_config={
        "Software Subjects": st.column_config.SelectboxColumn(
            "Software Subjects",
            help="The Software courses we provide",
            width="medium",
            options=[
            "📊 Software Design",
            "📈 Software Modeling",
            "🤖 Software Measurement",
            "📊 Requirement Engineering"
            ],
            required=True,
        )
    },
    hide_index=True,
)

# Function to find the most frequently selected item
def most_selected_item(df):
    if any(selected_subject):
        most_common_item = selected_subject["Software Subjects"].mode()[0]
        return most_common_item

# Return the most selected item if a selection is made
if any(selected_subject):
    most_selected = most_selected_item(selected_subject)
    st.write("Most selected item:", most_selected)

#_____________________________________________________________
st.title("9: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd

st.subheader("9: Example: st.column_config.SelectboxColumn")
df = pd.DataFrame(
     {
        "Software Subjects": [
            "📊 Software Design",
            "📈 Software Modeling",
            "🤖 Software Measurement",
            "📊 Requirement Engineering",
            "📊 Requirement Engineering",
        ],
    }
)

selected_subject = st.data_editor(
    df,
    column_config={
        "Software Subjects": st.column_config.SelectboxColumn(
            "Software Subjects",
            help="The Software courses we provide",
            width="medium",
            options=[
            "📊 Software Design",
            "📈 Software Modeling",
            "🤖 Software Measurement",
            "📊 Requirement Engineering"
            ],
            required=True,
        )
    },
    hide_index=True,
)

# Function to find the most frequently selected item
def most_selected_item(df):
    if any(selected_subject):
        most_common_item = selected_subject["Software Subjects"].mode()[0]
        return most_common_item

# Return the most selected item if a selection is made
if any(selected_subject):
    most_selected = most_selected_item(selected_subject)
    st.write("Most selected item:", most_selected)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.column_config.DatetimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, format=None, min_value=None, max_value=None, step=None, timezone=None)
st.subheader("10: Example: st.column_config.DatetimeColumn")

date_df = pd.DataFrame(
    {
        "Dates": [
            datetime(2024, 8, 8, 12, 30),
            datetime(2023, 7, 11, 18, 30),
            datetime(2010, 3, 12, 20, 20),
            datetime(2023, 11, 6, 3, 22),
        ],
        "Available": [True, False, True, True],

    }
)

date_available = st.data_editor(
    date_df,
    column_config={
        "Dates": st.column_config.DatetimeColumn(
            "Schedule",
            min_value=datetime(2010, 3, 12),
            max_value=datetime(2028, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
            help="Book your time",
            width=400,
        ),
    },
    hide_index=True,
)

# Display the the available dates
# Checkbox to fill data
fill_checkbox = st.checkbox("Show Available Dates", key="fill_checkbox")

# Text boxes to display row data
if fill_checkbox:
    selected_row_index = date_available[date_available["Available"] == True]
    st.write("The available dates:", selected_row_index)
else:
   st.write("There is no available dates:")

#_____________________________________________________________
st.title("10: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
from datetime import datetime

st.subheader("10: Example: st.column_config.DatetimeColumn")

date_df = pd.DataFrame(
    {
        "Dates": [
            datetime(2024, 8, 8, 12, 30),
            datetime(2023, 7, 11, 18, 30),
            datetime(2010, 3, 12, 20, 20),
            datetime(2023, 11, 6, 3, 22),
        ],
        "Available": [True, False, True, True],

    }
)

date_available = st.data_editor(
    date_df,
    column_config={
        "Dates": st.column_config.DatetimeColumn(
            "Schedule",
            min_value=datetime(2010, 3, 12),
            max_value=datetime(2028, 1, 1),
            format="D MMM YYYY, h:mm a",
            step=60,
            help="Book your time",
            width=400,
        ),
    },
    hide_index=True,
)

# Display the the available dates
# Checkbox to fill data
fill_checkbox = st.checkbox("Show Available Dates", key="fill_checkbox")

# Text boxes to display row data
if fill_checkbox:
    selected_row_index = date_available[date_available["Available"] == True]
    st.write("The available dates:", selected_row_index)
else:
   st.write("There is no available dates:")
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.column_config.DateColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, format=None, min_value=None, max_value=None, step=None)

st.subheader("11: Example: st.column_config.DateColumn")

date_df = pd.DataFrame(
    {
        "Date Invented": [date(1999, 2, 5), date(1980, 8, 13), date(1992, 5, 10), date(2002, 9, 11), ],
        "Programming": ["Python", "Java", "HTML", "C++"],
        "Difficult": ["Easy", "Hard", "Hard", "Easy"],
        "Available": [True, False, True, True],
    }
)

language_available = st.data_editor(
    date_df,
    column_config={
        "Date Invented": st.column_config.DateColumn(
            "Date Created",
            help="Date Invented for the languages",
            min_value=date(1960, 12, 12),
            max_value=date(2020, 12, 12),
            format="DD.MM.YYYY",
            step=1,
            width=400
        )
    },
    hide_index=True,
)

# Display the the available dates
# Checkbox to fill data
fill_checkbox = st.checkbox("Select Columns not to be Edited", key="fill_checkbox1")

# Text boxes to display row data
if fill_checkbox:
    select_setting_option = st.multiselect("Dont edit These Columns",language_available.columns.to_list())
    if select_setting_option:
      st.data_editor(language_available, disabled=(select_setting_option))

   # selected_language = language_available[language_available["Available"] == True]
   # st.write("The available dates:", selected_language)
else:
   st.write("All columns are editable:")


#_____________________________________________________________
st.title("11: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
from datetime import date

st.subheader("11: Example: st.column_config.DateColumn")

date_df = pd.DataFrame(
    {
        "Date Invented": [date(1999, 2, 5), date(1980, 8, 13), date(1992, 5, 10), date(2002, 9, 11), ],
        "Programming": ["Python", "Java", "HTML", "C++"],
        "Difficult": ["Easy", "Hard", "Hard", "Easy"],
        "Available": [True, False, True, True],
    }
)

language_available = st.data_editor(
    date_df,
    column_config={
        "Date Invented": st.column_config.DateColumn(
            "Date Created",
            help="Date Invented for the languages",
            min_value=date(1960, 12, 12),
            max_value=date(2020, 12, 12),
            format="DD.MM.YYYY",
            step=1,
            width=400
        )
    },
    hide_index=True,
)

# Display the the available dates
# Checkbox to fill data
fill_checkbox = st.checkbox("Select Columns not to be Edited", key="fill_checkbox1")

# Text boxes to display row data
if fill_checkbox:
    select_setting_option = st.multiselect("Dont edit These Columns",language_available.columns.to_list())
    if select_setting_option:
      st.data_editor(language_available, disabled=(select_setting_option))

   # selected_language = language_available[language_available["Available"] == True]
   # st.write("The available dates:", selected_language)
else:
   st.write("All columns are editable:")
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.column_config.TimeColumn(label=None, *, width=None, help=None, disabled=None, required=None, default=None, format=None, min_value=None, max_value=None, step=None)

st.subheader("12: Example: st.column_config.TimeColumn")

date_df = pd.DataFrame(
    {
        "Programming": ["Python", "Java", "HTML", "C++"],
        "Date Invented": [date(1999, 2, 5), date(1980, 8, 13), date(1992, 5, 10), date(2002, 9, 11)],
        "Class Period": [time(10, 40), time(12, 40), time(4, 33), time(20, 33)],
        "Difficult": ["Easy", "Hard", "Hard", "Easy"],
        "Available": [True, False, True, True],
    }
)

edited_df = st.data_editor(
    date_df,
    column_config={
        "Class Period": st.column_config.TimeColumn(
            "Class Time",
            help="This is course time",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
            width=100
        ),
    },
    hide_index=True,
)

# Checkbox to fill data
fill_checkbox = st.checkbox("Show available Classes", key="fill_checkbox2")

# Text boxes to display row data
if fill_checkbox:
   if any(edited_df["Available"]):
       st.write(edited_df[edited_df["Available"] == False])
   else:
      st.write("All Classes are available")


#_____________________________________________________________
st.title("11: Code of the Example above")

code_example = """import streamlit as st
import pandas as pd
from datetime import time

st.subheader("12: Example: st.column_config.TimeColumn")

date_df = pd.DataFrame(
    {
        "Programming": ["Python", "Java", "HTML", "C++"],
        "Date Invented": [date(1999, 2, 5), date(1980, 8, 13), date(1992, 5, 10), date(2002, 9, 11)],
        "Class Period": [time(10, 40), time(12, 40), time(4, 33), time(20, 33)],
        "Difficult": ["Easy", "Hard", "Hard", "Easy"],
        "Available": [True, False, True, True],
    }
)

edited_df = st.data_editor(
    date_df,
    column_config={
        "Class Period": st.column_config.TimeColumn(
            "Class Time",
            help="This is course time",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
            width=100
        ),
    },
    hide_index=True,
)

# Checkbox to fill data
fill_checkbox = st.checkbox("Show available Classes", key="fill_checkbox2")

# Text boxes to display row data
if fill_checkbox:
   if any(edited_df["Available"]):
       st.write(edited_df[edited_df["Available"] == False])
   else:
      st.write("All Classes are available")
"""
my_code(code_example)
st.divider()