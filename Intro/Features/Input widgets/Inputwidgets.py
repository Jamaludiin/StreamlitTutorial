import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

st.subheader("1: Example of st.button")

btn1 = st.button("Button one", type="primary")

if btn1:
    st.write('You clicked button one')
else:
    st.write('Click button one')
    
#-----------------------
if st.button('Button two'):
    st.write('You clicked button two')
else:
    st.write('Click button two')


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.button")

btn1 = st.button("Button one", type="primary")

if btn1:
    st.write('You clicked button one')
else:
    st.write('Click button one')
    
#-----------------------
if st.button('Button two'):
    st.write('You clicked button two')
else:
    st.write('Click button two')
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

st.subheader("2: Example of st.button with some properties")

st.button("Secondary Button 3",key=1,type="secondary",disabled=False,use_container_width=True)
st.button("Brimary Button 3",key=2,type="primary",disabled=False,use_container_width=True)

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.button with some properties")

st.button("Secondary Button 3",key=1,type="secondary",disabled=False,use_container_width=True)
st.button("Brimary Button 3",key=2,type="primary",disabled=False,use_container_width=True)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

st.subheader("3: Example of st.button with some practice")

st.title("Radio Buttons, Checkboxes and Buttons")
page_names = ['Checkbox','Button']

page = st.radio('Navigation', page_names)
st.write("**The variable 'page' returns:**",page)

if page == 'Checkbox':
  st.subheader("Welcome to the Checkbox page")
  st.write("Nice to see you! :wave:")
else:
  st.subheader("Welcome to the Button page")
  st.write(":thumbsup:") 


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.button with some practice")

st.title("Radio Buttons, Checkboxes and Buttons")
page_names = ['Checkbox','Button']

page = st.radio('Navigation', page_names)
st.write("**The variable 'page' returns:**",page)

if page == 'Checkbox':
  st.subheader("Welcome to the Checkbox page")
  st.write("Nice to see you! :wave:")
else:
  st.subheader("Welcome to the Button page")
  st.write(":thumbsup:") 
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)

st.subheader("4: Example of st.button with Nested practice")
check = st.checkbox("Click here")
st.write("State of the checkbox", check)

if check:
    nested_btn = st.button("Button Nested in Checkbox")
    if check:
      st.write(":smile:"*12)

else:
  st.subheader("Welcome to the Button page")
  st.write("Nice to see you! :thumbsup:")
  result = st.button("Click here")
  st.write("State of the button:",result)

  if result:
     nested_checkbox = st.checkbox("Checkbox Nested in Button")
     if nested_checkbox:
      st.write(":heart:"*20)
   
#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
st.subheader("4: Example of st.button with Nested practice")
check = st.checkbox("Click here")
st.write("State of the checkbox", check)

if check:
    nested_btn = st.button("Button Nested in Checkbox")
    if check:
      st.write(":smile:"*12)

else:
  st.subheader("Welcome to the Button page")
  st.write("Nice to see you! :thumbsup:")
  result = st.button("Click here")
  st.write("State of the button:",result)

  if result:
     nested_checkbox = st.checkbox("Checkbox Nested in Button")
     if nested_checkbox:
      st.write(":heart:"*20)
"""