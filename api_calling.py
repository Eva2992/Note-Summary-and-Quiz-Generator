from google import genai 
import streamlit as st 
from dotenv import load_dotenv 
import os  , io

from gtts import gTTS    #pip install gTTS  ()


#loading environment variables 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client

client = genai.Client(api_key=api_key)

#note generate 
def note_generate(images) :
    
    prompt = """Summarize the picture in note format at max 150 words
                     , make sure to add necessary markdown to differentiate different section """
    response = client.models.generate_content(
        model = "gemini-3-flash-preview" ,
        contents =  [images ,prompt]
    )

    return response.text 

def audio_translation(text) :

    speech = gTTS(text=text , lang ='en' , slow=False)

    speech.save("welcome.mp3") # saves to the local directory

    audio_buffer=io.BytesIO() # space in memory to hold the audio data

    speech.write_to_fp(audio_buffer) #temp audio data is written to the buffer

    st.audio(audio_buffer , format = "audio/mp3")

def quiz_generate(text , difficulty) :
    prompt = f"""Generate a quiz based on the following notes with {difficulty} difficulty level. 
                 Include 5 questions with 4 options each and provide the correct answer for each question.
                 Make sure to add necessary markdown to differentiate different section.
                 Notes: {text}"""

    response = client.models.generate_content(
        model = "gemini-3-flash-preview" ,
        contents =  [prompt]
    )

    return response.text
                     
        
