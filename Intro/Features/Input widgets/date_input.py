import streamlit as st


import datetime



#

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")

st.subheader("1: Example of st.date_input")

d = st.date_input("Tell me your appointment date", datetime.date(1995, 9, 12))
st.write('Your selected date is:', d)

st.subheader("Calculate your age")
Birth_date = st.date_input("Date of Birth", datetime.date(1995, 9, 12))
current_date = st.date_input("Current Date", datetime.date(2024, 3, 1))

if Birth_date is not None and Birth_date !='':
    new_age = current_date.year - Birth_date.year
    st.write('Your age is:', new_age, "Note: months and days was not calculated")
else:
    st.write("Fill the Birth date")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
import datetime

st.subheader("1: Example of st.date_input")

d = st.date_input("Tell me your appointment date", datetime.date(1995, 9, 12))
st.write('Your selected date is:', d)

st.subheader("Calculate your age")
Birth_date = st.date_input("Date of Birth", datetime.date(1995, 9, 12))
current_date = st.date_input("Current Date", datetime.date(2024, 3, 1))

if Birth_date is not None and Birth_date !='':
    new_age = current_date.year - Birth_date.year
    st.write('Your age is:', new_age, "Note: months and days was not calculated")
else:
    st.write("Fill the Birth date")

"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
from datetime import datetime

st.subheader("2: Example of st.date_input")

# Get the current date and time
current_datetime = datetime.now()
# Extract the date part from the current date and time
current_date = current_datetime.date()

# Print the current date
st.write("the current date",current_date)

# Print the current date and time
st.write("Current date and time:", current_datetime)
st.subheader("Today's Date")
Birth_date = st.date_input("Today's Date is", current_datetime)

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
import datetime
from datetime import datetime

st.subheader("2: Example of st.date_input")

# Get the current date and time
current_datetime = datetime.now()
# Extract the date part from the current date and time
current_date = current_datetime.date()

# Print the current date
st.write("the current date",current_date)

# Print the current date and time
st.write("Current date and time:", current_datetime)
st.subheader("Today's Date")
Birth_date = st.date_input("Today's Date is", current_datetime)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
from datetime import date

st.subheader("3: Example of st.date_input")

# Get the current date
current_date = datetime.now().date()

year = current_date.year
month = current_date.month
day = current_date.day

st.write("Year:",year,"Month:",month,"Day:",day)

#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
import datetime
from datetime import date

st.subheader("3: Example of st.date_input")

# Get the current date
current_date = datetime.now().date()

year = current_date.year
month = current_date.month
day = current_date.day

st.write("Year:",year,"Month:",month,"Day:",day)
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
from datetime import date


st.subheader("4: Example of st.date_input")

# Get the current date
current_date = datetime.now().date()

year = current_date.year
month = current_date.month
day = current_date.day

import datetime

age = st.date_input("Tell me you date of birth",datetime.date(1995, 3, 1))
st.date_input("Current date",current_date)

if st.button("Calculate",type='primary'):
 st.write("Year:",age.year - year,"Month:",age.month - month,"Day:",age.day - day)

 #_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
from datetime import date


st.subheader("4: Example of st.date_input")

# Get the current date
current_date = datetime.now().date()

year = current_date.year
month = current_date.month
day = current_date.day

import datetime

age = st.date_input("Tell me you date of birth",datetime.date(1995, 3, 1))
st.date_input("Current date",current_date)

if st.button("Calculate",type='primary'):
 st.write("Year:",age.year - year,"Month:",age.month - month,"Day:",age.day - day)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.date_input(label, value="today", min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, format="YYYY/MM/DD", disabled=False, label_visibility="visible")
from datetime import date

st.subheader("5: Example of st.date_input age calculation correctly")

# Get the current date
current_date = date.today()

# Get the date of birth from the user
dob = st.date_input("Tell me your date of birth", date(1995, 3, 1))

# Display the current date
st.date_input("Current date:", current_date)

if st.button("Calculate Age", type='primary'):
    # Calculate age
    age_year = current_date.year - dob.year
    age_month = current_date.month - dob.month
    age_day = current_date.day - dob.day

    # Adjust age if current month or day is earlier than birth month or day
    if current_date.month < dob.month or (current_date.month == dob.month and current_date.day < dob.day):
        age_year -= 1
        age_month = 12 - abs(age_month)
    
    if age_day < 0:
        age_month -= 1
        age_day = 30 - abs(age_day)

    st.write("Age :", age_year, "years,", age_month, "months,", age_day, "days")


 #_____________________________________________________________
st.title("5: Code of the Example above")

code_example = """import streamlit as st
from datetime import date

st.subheader("5: Example of st.date_input age calculation correctly")

# Get the current date
current_date = date.today()

# Get the date of birth from the user
dob = st.date_input("Tell me your date of birth", date(1995, 3, 1))

# Display the current date
st.date_input("Current date:", current_date)

if st.button("Calculate Age", type='primary'):
    # Calculate age
    age_year = current_date.year - dob.year
    age_month = current_date.month - dob.month
    age_day = current_date.day - dob.day

    # Adjust age if current month or day is earlier than birth month or day
    if current_date.month < dob.month or (current_date.month == dob.month and current_date.day < dob.day):
        age_year -= 1
        age_month = 12 - abs(age_month)
    
    if age_day < 0:
        age_month -= 1
        age_day = 30 - abs(age_day)

    st.write("Age :", age_year, "years,", age_month, "months,", age_day, "days")
"""
my_code(code_example)
st.divider()