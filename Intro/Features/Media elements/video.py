import streamlit as st


# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.video(data, format="video/mp4", start_time=0)

st.subheader("1: Example of st.video")

video_file = open('file_example_MP4_480_1_5MG.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes,format="video/mp4", start_time=0)



#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.video")

video_file = open('file_example_MP4_480_1_5MG.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes,format="video/mp4", start_time=0)
"""
my_code(code_example)
st.divider()