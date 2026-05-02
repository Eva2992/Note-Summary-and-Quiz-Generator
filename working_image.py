from google import genai 
import streamlit as st 
from dotenv import load_dotenv 
import os 
from PIL import Image # for image processing , images cannot directly be passed to genai model

#loading environment variables 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the Gemini API client

client = genai.Client(api_key=api_key)

images = st.file_uploader("Upload your notes here" ,
                     type =['jpg' , 'jpeg' , 'png'] ,
                      accept_multiple_files=True )




if images :
    
    pil_images = []
    for img in images :
        pil_image = Image.open(img)
        pil_images.append(pil_image)
        
    prompt = """Summarize the picture in note format aat max 100 words
                     , make sure to add necessary markdown to differentiate different section """
    response = client.models.generate_content(
        model = "gemini-3-flash-preview" ,
        contents =  [images ,prompt]
    )

    st.text(response.text)