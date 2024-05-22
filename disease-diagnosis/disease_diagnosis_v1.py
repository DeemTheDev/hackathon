import streamlit as st
import pandas as pd
import io
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image
import requests

ms = st.session_state
if "themes" not in ms: 
    ms.themes = {"current_theme": "light",
                "refreshed": True,
                
                "light": {"theme.base": "dark",
                        "theme.backgroundColor": "#0E1117",
                        "theme.primaryColor": "#FF4B4B",
                        "theme.secondaryBackgroundColor": "#262730",
                        "theme.textColor": "white",
                        "button_face": "Switch to Dark Mode"},

                "dark":  {"theme.base": "light",
                        "theme.backgroundColor": "#FFFFFF",
                        "theme.primaryColor": "#FF4B4B",
                        "theme.secondaryBackgroundColor": "#F0F2F6",
                        "theme.textColor": "#31333F",
                        "button_face": "Switch to Light Mode"},
                }


def ChangeTheme():
    previous_theme = ms.themes["current_theme"]
    tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
    for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)

    ms.themes["refreshed"] = False
    if previous_theme == "dark": 
        ms.themes["current_theme"] = "light"
    elif previous_theme == "light": 
        ms.themes["current_theme"] = "dark"


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY = 'AIzaSyAvw5v7lTEkG06xwNTNG69outIzHKV4yO0'
genai.configure(api_key=GOOGLE_API_KEY)

def diagnose_disease(image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["What is in the picture? ", image], stream=True)
    response.resolve()
    return response.text

def main():
    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
        ms.themes["refreshed"] = True
        st.rerun()

    st.markdown("<h1 style='text-align: center;'>Hello, Welcome to Disease Diagnosis</h1>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        img = PIL.Image.open(io.BytesIO(uploaded_file.read())) 
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Loading spinner while diagnosis is being processed
        with st.spinner("Diagnosing..."):
            result = diagnose_disease(img)
        
        # Display diagnosis result
        st.markdown(f"Diagnosis Result: {result}")

if __name__ == "__main__":
    main()
