import streamlit as st 
from api_calling import note_generate
from api_calling import audio_translation
from api_calling import quiz_generate
st.set_page_config(layout="wide")
from PIL import Image         # for image processing , images cannot directly be passed to genai model 

st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate a summary and quiz")
st.divider()

with st.sidebar :
    st.header("Controls")
    images = st.file_uploader("Upload your notes here" ,
                     type =['jpg' , 'jpeg' , 'png'] ,
                      accept_multiple_files=True )

    if images : 
        pil_images = []
        for img in images :
            pil_image = Image.open(img)
            pil_images.append(pil_image)
         
        if len(images) > 3 :
            st.error("Please upload a maximum of 3 images.")
        else :
            st.subheader("Uploaded Images")
            col = st.columns(len(images)) 
            for i , img in enumerate(images) :
                with col[i] :
                    st.image(img)   

    selected_option = st.selectbox("Enter the difficulty of Quiz" ,
             ("Easy" , "Medium" , "Hard") , 
             index = None)              



    pressed =st.button("Generate Summary and Quiz", type = "primary")



if pressed :
   if not images :
      st.error("Please upload at least one image to generate the summary and quiz.")

   if not selected_option :
      st.error("Please select a difficulty level for the quiz.")
   
   if images and selected_option :

      # note 
      with st.container(border= True ) :
         st.subheader("Yout note")
         with st.spinner("Generating your note summary...") :
          generated_note = note_generate(pil_images) 
          st.markdown(generated_note) 
   
   
   #quiz
      with st.container(border = True)  :
         st.subheader(f"Quiz  ({selected_option}) Difficulty")
         with st.spinner("Generating Your Quiz ...") :
            generated_quiz=quiz_generate(generated_note , selected_option)

            st.markdown(generated_quiz)



      # Audio 
      
      with st.container(border = True)  :
         st.subheader("Audio Transcription")
         with st.spinner("Generating audio transcription.Please wait ,Sometimes it takes little too long ...") :
            #cleaning markdown 
            generated_note = generated_note.replace("#" , "")
            generated_note = generated_note.replace("*" , "")
            generated_note = generated_note.replace("-" , "")
            generated_note = generated_note.replace("-" , " ")

            audio_translation(generated_note)
          

      










# python -m venv projectview  --for creating virtual environment

# pip install streamlit

# pip install google-genai

# pip install python-dotenv

# .\\.venv\\Scripts\\Activate.ps1  -- to activate virtual environment ( from Quizify directory)

# streamlit run app.py -- to run the streamlit app

