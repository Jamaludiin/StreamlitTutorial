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
st.title("5: Code of the Example above")

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

#------------------------------------------------------------
# syntax 
# st.subheader(body, anchor=None, *, help=None, divider=False)

st.title("6: Example of st.subheader")

st.subheader("This is subheader",anchor=False, help="Markdown")

#_____________________________________________________________
st.title("6: Code of the Example above")

code_example = """import streamlit as st

st.subheader("This is subheader",anchor=False, help="Markdown")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.caption(body, unsafe_allow_html=False, *, help=None)

st.title("7: Example of st.caption")

st.subheader("This is caption", help="caption help")

#_____________________________________________________________
st.title("7: Code of the Example above")

code_example = """import streamlit as st

st.subheader("This is caption", help="caption help")
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.text(body, *, help=None)

st.title("8: Example of st.text")

st.text("This is text element", help="text help")

#_____________________________________________________________
st.title("8: Code of the Example above")

code_example = """import streamlit as st

st.text("This is text element", help="text help")
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.latex(body, *, help=None)

st.title("9: Example of st.latex element")

st.latex("This is latex element", help="latex help")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

#_____________________________________________________________
st.title("9: Code of the Example above")

code_example = """import streamlit as st

st.latex("This is text element", help="latex help")
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.write(*args, unsafe_allow_html=False, **kwargs)

st.title("10: Example of st.write element")

st.write("This is write element.", unsafe_allow_html=False,)

#_____________________________________________________________
st.title("10: Code of the Example above")

code_example = """import streamlit as st

st.write("This is write element.", unsafe_allow_html=False,)
"""
my_code(code_example)
st.divider()