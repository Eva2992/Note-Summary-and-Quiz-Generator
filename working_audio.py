from gtts import gTTS    #pip install gTTS
import streamlit as st
import io  
   
text = "Hello, this is a sample text to convert to speech using gTTS library in Python."

speech = gTTS(text=text , lang ='en' , slow=False)

speech.save("welcome.mp3") # saves to the local directory

audio_buffer=io.BytesIO() # space in memory to hold the audio data

speech.write_to_fp(audio_buffer) #temp audio data is written to the buffer

st.audio(audio_buffer , format = "audio/mp3")




          