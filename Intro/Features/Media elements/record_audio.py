import streamlit as st
from st_audiorec import st_audiorec

# def
def my_code(code):
    st.code(f"""{code}""")

#------------------------------------------------------------
# syntax 
# st.audio(data, format="audio/wav", start_time=0, *, sample_rate=None)

st.subheader("1: Example of st.audio")

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')