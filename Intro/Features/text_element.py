import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏴󠁧󠁢󠁥󠁮󠁧󠁿",
)

# def
def my_code(code):
    st.code(f"""{code}""")


# text ELEMENTS
#------------------------------------------------------------
st.title("1: Example of st.code")

# syntax of st.code
# st.code(body, language="python", line_numbers=False)

code = '''import streamlit as st
def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python', line_numbers=True)

#_____________________________________________________________
st.title("1: Code of the Example above")

# Example usage
code_example = """
import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''

st.code(code, language='python', line_numbers=True)
"""

my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.markdown(body, unsafe_allow_html=False, *, help=None)

st.title("2: Example of st.markdown")

st.markdown("Markdown My Python",unsafe_allow_html=False, help="Markdown")

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st

st.markdown("Markdown My Python",unsafe_allow_html=False, help="Markdown")
"""
my_code(code_example)
st.divider()

#--------------------------text_area----------------------------------
st.title("3: Example of st.text_area")
# more 
st.text_area('Type in your text string',
                  "Happy Streamlit st.text_area")

#_____________________________text_area________________________________
st.title("3: Code of the Example above")

code_example = """ import streamlit as st
st.markdown("Markdown My Python",unsafe_allow_html=False, help="Markdown")
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.title(body, anchor=None, *, help=None)

st.title("4: Example of st.title")

st.title("This is Title",anchor=False, help="Markdown")
st.title("Another Title",anchor="String", help=False)


#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st

st.title("This Title",anchor=False, help="Markdown")
st.title("Another Title",anchor="String", help=False)
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.header(body, anchor=None, *, help=None, divider=False)

st.title("5: Example of st.header")

st.header('**Example App showing Anchor links**',help="Header Help")

st.markdown('''
# Sections
- [Section 1](#section-1)
- [Section 2](#section-2)
''', unsafe_allow_html=True)

st.header('Section 1')
st.header('Section 2')

#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st

st.header('**Example App showing Anchor links**',help="Header Help")

st.markdown('''
# Sections
- [Section 1](#section-1)
- [Section 2](#section-2)
''', unsafe_allow_html=True)

st.header('Section 1')
st.header('Section 2')
"""
my_code(code_example)
st.divider()