# installed these
# pip install streamlit-mic-recorder
# pip install streamlit-audiorec


import streamlit as st
from st_audiorec import st_audiorec
from streamlit_mic_recorder import mic_recorder,speech_to_text

# record_audio
# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("1: Example of st_audiorec")

st.subheader("Using the package made by Stefan https://github.com/stefanrmmr/streamlit-audio-recorder")
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')


#_____________________________________________________________
st.title("1: Code of the Example above")

code_example = """import streamlit as st
from st_audiorec import st_audiorec

st.subheader("1: Example of st_audiorec")

st.subheader("Using the package made by Stefan https://github.com/stefanrmmr/streamlit-audio-recorder")
wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
"""
my_code(code_example)
st.divider()

#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("2: Example of mic_recorder")
audio=mic_recorder(
    start_prompt="Start recording",
    stop_prompt="Stop recording", 
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
)

if audio:       
    st.audio(audio['bytes'])
    #st.audio(audio)
#_____________________________________________________________
st.title("2: Code of the Example above")

code_example = """import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text

st.subheader("2: Example of mic_recorder")


audio=mic_recorder(
    start_prompt="Start recording",
    stop_prompt="Stop recording", 
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
)

if audio:       
    st.audio(audio['bytes'])
"""
my_code(code_example)
st.divider()



#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("3: Example of mic_recorder USING ICON BUTTON")

st.write("Record your voice, and play the recorded audio:")
audio=mic_recorder(start_prompt="⏺️",stop_prompt="⏹️",key='recorder')

if audio:       
    st.audio(audio['bytes'])



#_____________________________________________________________
st.title("3: Code of the Example above")

code_example = """import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text

st.subheader("3: Example of mic_recorder USING ICON BUTTON")

st.write("Record your voice, and play the recorded audio:")
audio=mic_recorder(start_prompt="⏺️",stop_prompt="⏹️",key='recorder')

if audio:       
    st.audio(audio['bytes'])
"""
my_code(code_example)
st.divider()





#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("4: Example of speech_to_text")
st.subheader("This is another way of speech_to_text")

state=st.session_state

if 'text_received' not in state:
    state.text_received=[]

c1,c2=st.columns(2)
with c1:
    st.write("Convert speech to text:")
with c2:
    text=speech_to_text(language='en',use_container_width=True,just_once=True,key='STT')

if text:       
    state.text_received.append(text)

for text in state.text_received:
    st.text(text)



#_____________________________________________________________
st.title("4: Code of the Example above")

code_example = """import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text

st.subheader("4: Example of speech_to_text")
st.subheader("This is another way of speech_to_text")

state=st.session_state

if 'text_received' not in state:
    state.text_received=[]

c1,c2=st.columns(2)
with c1:
    st.write("Convert speech to text:")
with c2:
    text=speech_to_text(language='en',use_container_width=True,just_once=True,key='STT')

if text:       
    state.text_received.append(text)

for text in state.text_received:
    st.text(text)
"""
my_code(code_example)
st.divider()



"""

import streamlit as st
import sounddevice as sd
import numpy as np

state = st.session_state

if 'audio_data' not in state:
    state.audio_data = []

st.write("Record your voice:")

if st.button("Start Recording"):
    duration = 5  # Recording duration in seconds
    fs = 44100  # Sampling frequency
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()  # Wait for the recording to complete
    state.audio_data.append(recording)

if st.button("Stop Recording"):
    st.write("Recording stopped.")
    sd.stop()

for audio in state.audio_data:
    st.audio(audio, format="audio/wav")
"""