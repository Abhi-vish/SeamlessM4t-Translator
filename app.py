import streamlit as st
from engine import Translate
import os
import shutil
import json

translator = Translate()
# Creating the list of the tasks the seamlessM4t model can perform
tasks = ['S2ST (Speech to Speech translation)',
        'S2TT (Speech to Text translation)',
        'T2ST (Text to Speech translation)',
        'T2TT (Text to Text translation)']

def move_audio_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        return True  # Return True if the move was successful
    except Exception as e:
        print(f"Error moving the audio file: {str(e)}")
        return False  # Return False if there was an error

# List of language options
languages = [
    "Catalan",
    "Czech",
    "Danish",
    "Dutch",
    "English",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Hindi",
    "Indonesian",
    "Italian",
    "Japanese",
    "Korean",
    "Maltese",
    "Mandarin Chinese",
    "Modern Standard Arabic",
    "Northern Uzbek",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Slovak",
    "Spanish",
    "Swahili",
    "Swedish",
    "Tagalog",
    "Telugu",
    "Thai",
    "Turkish",
    "Ukrainian",
    "Urdu",
    "Vietnamese",
    "Welsh",
    "Western Persian"
]

st.title("Seamless-M4t Translator")
task = st.selectbox('Select Task:', tasks)

if task == 'S2ST (Speech to Speech translation)':
    upload_audio = st.file_uploader('Upload Audio file', type=['mp3', 'wav', 'ogg'])
    target_language = st.selectbox('Target language:', languages)

    button_clicked = st.button('Convert')
    if button_clicked:
        if upload_audio and target_language:
            result = translator.translate(task=task, audio=upload_audio, target_language=target_language)
            
            # Set the source and destination paths for moving the audio file
            source_path = result.replace("\\", "/")
            audio_paths = source_path.split(',')
            for audio_path in audio_paths:
                try:
                    audio_path = audio_path.lstrip("['")
                    st.audio(audio_path.strip('"'), format="audio/*")
                    
                except Exception as e:
                    # audio_content = audio_path.lstrip(']')
                    audio_content=audio_path.rstrip(']')
                    st.write(audio_content)


elif task == 'S2TT (Speech to Text translation)':
    upload_audio = st.file_uploader('Upload Audio file', type=['mp3', 'wav', 'ogg'])
    # Create a button
    target_language = st.selectbox('Target language : ', languages)
    button_clicked = st.button("Convert")

    if button_clicked:
        if upload_audio:
            result = translator.translate(task=task, audio=upload_audio, target_language=target_language)
            result = json.loads(result)
            st.write(result)


elif task == 'T2ST (Text to Speech translation)':
    input_language = st.selectbox("Input Language:", languages)
    text = st.text_area("Enter the Text Here:")
    target_language = st.selectbox('Target language:', languages)

    button_clicked = st.button('Convert')

    if button_clicked:
        if text and input_language and target_language:
            result = translator.translate(task=task, text=text, input_language=input_language, target_language=target_language)
            
            # Set the source and destination paths for moving the audio file
            source_path = result.replace("\\", "/")
            audio_paths = source_path.split(',')
            for audio_path in audio_paths:
                try:
                    audio_path = audio_path.lstrip("['")
                    st.audio(audio_path.strip('"'), format="audio/wav")
                    
                except Exception as e:
                    # audio_content = audio_path.lstrip(']')
                    audio_content=audio_path.rstrip(']')
                    st.write(audio_content)

                
elif task == 'T2TT (Text to Text translation)':
    input_language = st.selectbox("Input Language:", languages)
    text = st.text_area("Enter the Text Here:")
    target_language = st.selectbox('Target language:', languages)

    button_clicked = st.button('Convert')

    if button_clicked:
        if text and input_language and target_language:
            result = translator.translate(task=task, text=text, input_language=input_language, target_language=target_language)
            conv = json.loads(result)
            st.write(conv[1])
