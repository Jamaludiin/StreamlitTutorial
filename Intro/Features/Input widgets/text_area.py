import streamlit as st

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("1: Example of st.text_area")

st.text_area(label="Put your text Notes in here", height=200, max_chars=2000, placeholder="My plan in this week is good enough",label_visibility="visible")

st.write("This is another text area with hidden labe visiblity")


st.text_area(label="Write some text in here", 
             height=100, 
             max_chars=1500, 
             placeholder="In literary theory, a text is any object that can be read, whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some",
             label_visibility="visible")


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.text_area")

st.text_area(label="Put your text Notes in here", height=200, max_chars=2000, placeholder="My plan in this week is good enough",label_visibility="visible")

st.write("This is another text area with hidden labe visiblity")


st.text_area(label="Write some text in here", 
             height=100, 
             max_chars=1500, 
             placeholder="In literary theory, a text is any object that can be read, whether this object is a work of literature, a street sign, an arrangement of buildings on a city block, or styles of clothing. It is a coherent set of signs that transmits some",
             label_visibility="visible")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("2: Example of st.text_area")

txt1 = st.text_area(label="Put your text or notes in here", height=200, max_chars=2000, placeholder="My plan in this week is good enough",label_visibility="visible")

if txt1 is not None and txt1 != '':
    st.write("You have typed these text: ",txt1)
else:
    st.write("Type a text first",txt1)


st.subheader("This is another text area")


txt2 = st.text_area(label="Write your ideas in here", 
             height=100, 
             max_chars=1500, 
             placeholder="In literary theory, a text is any object that can be read, whether this object is a work of literature, a street sign, an arrangement of buildings on a city block.",
             label_visibility="visible")

if st.button("Show the text"):
    if txt1 is not None and txt2 != '':
     st.write("You have typed this text: ",txt2)
    else:
     st.write("Better you type a text first",txt2)


#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.text_area")

txt1 = st.text_area(label="Put your text or notes in here", height=200, max_chars=2000, placeholder="My plan in this week is good enough",label_visibility="visible")

if txt1 is not None and txt1 != '':
    st.write("You have typed these text: ",txt1)
else:
    st.write("Type a text first",txt1)


st.subheader("This is another text area")


txt2 = st.text_area(label="Write your ideas in here", 
             height=100, 
             max_chars=1500, 
             placeholder="In literary theory, a text is any object that can be read, whether this object is a work of literature, a street sign, an arrangement of buildings on a city block.",
             label_visibility="visible")

if st.button("Show the text"):
    if txt1 is not None and txt2 != '':
     st.write("You have typed this text: ",txt2)
    else:
     st.write("Better you type a text first",txt2)
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")

st.subheader("3: Example of st.text_area")
txt = st.text_area(
    "The lengeth of this text",
    """literary theory, a text is any object that can be read, whether this object is a work of literature, 
    a street sign, an arrangement of buildings on a city block""",
    )

st.write(f'Your text size is {len(txt)} characters.')


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
txt = st.text_area(
    "The lengeth of this text", literary theory, a text is any object that can be read, whether this object is a work of literature, \na street sign, an arrangement of buildings on a city block" )

st.write(f'Your text size is {len(txt)} characters.')
"""
my_code(code_example)
st.divider()