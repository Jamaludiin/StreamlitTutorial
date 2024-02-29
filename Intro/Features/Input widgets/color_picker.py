import streamlit as st
import random


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.color_picker")

color = st.color_picker('Select a color', '#00f900', disabled=False)
st.write('You selected this color:', color)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.color_picker")

color = st.color_picker('Select a color', '#00f900', disabled=False)
st.write('You selected this color:', color)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("2: Example of st.color_picker")
a = 5
for i in range(a):
    st.color_picker(f'Color {i+1}:','#00f900')


a = 10
columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    column.color_picker(f'Color: {i+1}:', '#00f900')


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.color_picker")
a = 5
for i in range(a):
    st.color_picker(f'Color {i+1}:','#00f900')


a = 10
columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    column.color_picker(f'Color: {i+1}:', '#00f900')
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("3: Example of st.color_picker")
a = 10
columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate a random hex color
    column.color_picker(f'Color {i+1}:', random_color)  # Assign the random color to the color picker


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.color_picker")
a = 10
columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate a random hex color
    column.color_picker(f'Color {i+1}:', random_color)  # Assign the random color to the color picker
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")

st.subheader("4: Example of st.color_picker")
a = 5
col1,col2= st.columns([9,1])
with col1:
    for i in range(a):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        st.color_picker(f'{i+1}:',random_color)
        # Generate a random hex color
        #column.color_picker(f'Color {i+1} :', random_color)

with col2:
    for i in range(a):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        st.color_picker(f'{i+1} :',random_color)
        # Generate a random hex color
        #column.color_picker(f'Color {i+1} :', random_color)


a = 10

columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate a random hex color
    column.color_picker(f'{i+1}:', random_color)


#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
st.subheader("4: Example of st.color_picker")
a = 5
col1,col2= st.columns([9,1])
with col1:
    for i in range(a):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        st.color_picker(f'{i+1}:',random_color)
        # Generate a random hex color
        #column.color_picker(f'Color {i+1} :', random_color)

with col2:
    for i in range(a):
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        st.color_picker(f'{i+1} :',random_color)
        # Generate a random hex color
        #column.color_picker(f'Color {i+1} :', random_color)


a = 10

columns = st.columns(a)  # Create a set of horizontal columns

for i, column in enumerate(columns):
    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate a random hex color
    column.color_picker(f'{i+1}:', random_color)
"""
my_code(code_example)
st.divider()