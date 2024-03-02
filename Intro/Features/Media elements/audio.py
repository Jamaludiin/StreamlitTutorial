import streamlit as st
import numpy as np

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("1: Example of st.audio")

st.subheader("First Audio")
audio_file = open('sample.mp3', 'rb')
st.audio(audio_file, format='audio/mp3')


st.subheader("Second Audio")
audio_file = open('sample.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')

#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
st.subheader("1: Example of st.audio")

st.subheader("First Audio")
audio_file = open('sample.mp3', 'rb')
st.audio(audio_file, format='audio/mp3')


st.subheader("Second Audio")
audio_file = open('sample.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3')
"""
my_code(code_example)
st.divider()


#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("2: Example of st.audio Download")

st.subheader("First Audio to Download")
audio_path = open('sample.mp3', 'rb')
st.audio(audio_path, format='audio/mp3')
    

# Add a download link for the image
st.download_button('Download Audio', 
                   data = audio_path,
                   #'/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/sample.mp3',
                   disabled=False,
                   use_container_width=True,
                   file_name='sample.mp3',
                   mime='audio/mp3',
                   type="primary")

#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
st.subheader("2: Example of st.audio Download")

st.subheader("First Audio to Download")
audio_path = open('sample.mp3', 'rb')
st.audio(audio_path, format='audio/mp3')
    

# Add a download link for the image
st.download_button('Download Audio', 
                   data = audio_path,
                   #'/Users/jamalabdullahi/Python Tutorial/StreamlitTutorial/Intro/Features/Media elements/sample.mp3',
                   disabled=False,
                   use_container_width=True,
                   file_name='sample.mp3',
                   mime='audio/mp3',
                   type="primary")
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("3: Example of st.audio Play Audio")

st.subheader("First Audio to Play")

if st.button("Play"):
    audio_path = open('sample.mp3', 'rb')
    st.audio(audio_path, format='audio/mp3')


st.subheader("First Auto Audio Play Not working also")
# or
# Initialize a boolean variable to control audio playback
play_audio = False

# Display the "Play" button
if st.button("AutoPlay"):
    play_audio = True

# Check if the audio should be played
if play_audio:
    # Open the audio file
    with open('sample.mp3', 'rb') as audio_file:
        audio_bytes = audio_file.read()

    # Display the audio player
    st.audio(audio_bytes, format='audio/mp3', start_time=0)


#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
st.subheader("3: Example of st.audio Play Audio")

st.subheader("First Audio to Play")

if st.button("Play"):
    audio_path = open('sample.mp3', 'rb')
    st.audio(audio_path, format='audio/mp3')


st.subheader("First Auto Audio Play Not working also")
# or
# Initialize a boolean variable to control audio playback
play_audio = False

# Display the "Play" button
if st.button("AutoPlay"):
    play_audio = True

# Check if the audio should be played
if play_audio:
    # Open the audio file
    with open('sample.mp3', 'rb') as audio_file:
        audio_bytes = audio_file.read()

    # Display the audio player
    st.audio(audio_bytes, format='audio/mp3', start_time=0)
"""
my_code(code_example)
st.divider()