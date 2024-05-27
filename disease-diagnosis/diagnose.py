import io
import textwrap
import PIL.Image
import streamlit as st
import google.generativeai as genai
from IPython.display import Markdown


#Diagnosis Tabs:
testDiagnose, imagesDiagnose, pdfDaiagnose = st.tabs(["Diagnose Text", "Diagnose Image", "Diagnose PDF"])

#API KEYS:
TEXT_API_KEY = 'AIzaSyAvw5v7lTEkG06xwNTNG69outIzHKV4yO0'


#----------TEXT DIAGNOSIS----------
with testDiagnose:
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

    #Initialize chat session for text generation
    if 'text_chat_session' not in st.session_state:
        st.session_state.text_chat_session = text_model.start_chat(history=[])
        st.session_state.text_chat_history = []
    
    
    #This sends prompt to the API using streamlit and generative models .start_chat method
    def generate_text_response(text_input):
        response = st.session_state.text_chat_session.send_message(text_input)
        return response.text

    #Text only input:
    text_input = st.chat_input("Enter your text here:", key="text_chat")

    #Display chat history 
    st.markdown("### Chat History")
    for chat in st.session_state.text_chat_history:
        st.chat_message(chat["role"]).write(chat["content"])

    #Appends input to api chat history and stores as user role for streamlit 
    if text_input:
        st.session_state.text_chat_history.append({
            "role": "user",
            "content": text_input
            })
    
    #Generates response and store to chat history as assistant role
        with st.spinner("Generating response..."):
            response = generate_text_response(text_input)
            st.session_state.text_chat_history.append({
            "role": "assistant",
            "content": response
            })
        st.markdown(response)
        st.rerun()
#----------TEXT DIAGNOSIS----------

#----------END---------------------

#----------IMAGE DIAGNOSIS---------
with imagesDiagnose:
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
    image_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

    #Initialize chat session for text generation
    if 'image_chat_session' not in st.session_state:
        st.session_state.image_chat_session = text_model.start_chat(history=[])
        st.session_state.image_chat_history = []
    
    
    #This sends prompt to the API about image and returns a response
    def generate_image_response(prompt, image):
        response = image_model.generate_content([prompt, image], stream=True)
        response.resolve()
        return response.text


    #Text and image only input:
    image_text_input = st.chat_input("Enter your text here:", key="image_chat")

    #Image input
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        bytes_data = uploaded_image.getvalue()

        #Image READY FOR AI
        image = PIL.Image.open(io.BytesIO(bytes_data))
    else:
        image = None

    #Display chat history 
    st.markdown("### Chat History")
    for chat in st.session_state.image_chat_history:
        st.chat_message(chat["role"]).write(chat["content"])

    #Appends input to api chat history and stores as user role for streamlit 
    if image_text_input:
        st.session_state.image_chat_history.append({
            "role": "user",
            "content": image_text_input
            })
        st.image(image, caption='Uploaded Image', use_column_width=True)
    #Generates response and store to chat history as assistant role
        with st.spinner("Generating response..."):
            response = generate_image_response(image_text_input, image)
            st.session_state.image_chat_history.append({
            "role": "assistant",
            "content": response
            })
        st.markdown(response)
        st.rerun()

#----------IMAGE DIAGNOSIS----------
#----------END----------------------

#----------PDF DIAGNOSIS------------



        



