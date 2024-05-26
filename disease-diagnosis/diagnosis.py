import streamlit as st
from streamlit.web import cli
import io
import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image
import os

#API Keys
#Ashish's Text API
TEXT_API_KEY = 'AIzaSyCmemqNb7MRDsllKLm2cNdZClgeX6RrmDA'
#Nadeem's Image API
IMAGE_API_KEY = 'AIzaSyAvw5v7lTEkG06xwNTNG69outIzHKV4yO0'

# For the text generation
genai.configure(api_key=TEXT_API_KEY)

# Model configuration for text generation
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
#Safety Measures for AI
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

# Initialize the model for text generation
text_model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# Initialize chat session for text generation
if 'chat_session' not in st.session_state:
    st.session_state.chat_session = text_model.start_chat(history=[])

# Initialize session state for themes and chat history + Light mode and dark mode Config
if "themes" not in st.session_state:
    st.session_state.themes = {
        "current_theme": "light",
        "refreshed": True,
        "light": {
            "theme.base": "dark",
            "theme.backgroundColor": "#0E1117",
            "theme.primaryColor": "#FF4B4B",
            "theme.secondaryBackgroundColor": "#262730",
            "theme.textColor": "white",
            "button_face": "Switch to Dark Mode"
        },
        "dark": {
            "theme.base": "light",
            "theme.backgroundColor": "#FFFFFF",
            "theme.primaryColor": "#FF4B4B",
            "theme.secondaryBackgroundColor": "#F0F2F6",
            "theme.textColor": "#31333F",
            "button_face": "Switch to Light Mode"
        }
    }
    st.session_state.chat_history = []

def ChangeTheme():
    previous_theme = st.session_state.themes["current_theme"]
    tdict = st.session_state.themes["light"] if st.session_state.themes["current_theme"] == "light" else st.session_state.themes["dark"]
    for vkey, vval in tdict.items():
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)
    st.session_state.themes["refreshed"] = False
    st.session_state.themes["current_theme"] = "dark" if previous_theme == "light" else "light"

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def generate_text_response(user_input):
    response = st.session_state.chat_session.send_message(user_input)
    return response.text

# Separate function to configure and use the image diagnosis API
def diagnose_disease(image):
    genai.configure(api_key=IMAGE_API_KEY)  # Reconfigure API for image processing
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["What is in the picture? ", image], stream=True)
    response.resolve()
    return response.text

def main():
    btn_face = st.session_state.themes["light"]["button_face"] if st.session_state.themes["current_theme"] == "light" else st.session_state.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if st.session_state.themes["refreshed"] == False:
        st.session_state.themes["refreshed"] = True
        st.rerun()

    st.markdown("<h1 style='text-align: center;'>Hello, Welcome to Disease Diagnosis</h1>", unsafe_allow_html=True)

    # Input field for text messages
    user_input = st.text_input("Enter your message here:")
    submit_text = st.button("Submit Text")

    # Image upload button
    uploaded_file = st.file_uploader("Choose an image file")
    submit_image = st.button("Submit Image")

    # Display chat history
    st.markdown("### Chat History")
    for chat in st.session_state.chat_history:
        st.markdown(chat)

    if submit_text and user_input:
        st.session_state.chat_history.append(f"**User:** {user_input}")
        with st.spinner("Generating response..."):
            response = generate_text_response(user_input)
        st.session_state.chat_history.append(f"**DR. AI:** {response}")
        st.rerun()

    if submit_image and uploaded_file is not None:
        st.session_state.chat_history.append(f"**User:** [Image Uploaded]")
        bytes_data = uploaded_file.getvalue()
        img = PIL.Image.open(io.BytesIO(bytes_data))
        st.image(img, caption='Uploaded Image', use_column_width=True)
        with st.spinner("Diagnosing..."):
            result = diagnose_disease(img)
        st.session_state.chat_history.append(f"**AI:** {result}")
        st.rerun()

    if submit_image and uploaded_file is None:
        st.error("Please upload an image file before submitting.")

if __name__ == "__main__":
    main()
