# -*- coding: utf-8 -*-
# GOOGLE IMPORTS FOR IMAGES AND TEXT
import io
import json
import PIL.Image
import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
#import Machine Learning Algorithm

#Animation
left_column, right_column = st.columns(2)

with left_column:
    st.header("""
                  
            An AI-Powered disease Diagnosis Tool
                  
        """)

with right_column:
    with open("./assets/animation-d.json", "r") as a:
        animation = json.load(a)
    st_lottie(animation, quality='high', height=160)

#Side Navigation Bar
st.sidebar.title('Navigation')
st.sidebar.link_button('Home', url="http://localhost:5173/")
treatment =st.sidebar.link_button('Treatment Plan', "http://localhost:8502/")



# Diagnosis Tabs:

testDiagnose, imagesDiagnose = st.tabs(["𝗗𝗶𝗮𝗴𝗻𝗼𝘀𝗲 𝗧𝗲𝘅𝘁", "𝗗𝗶𝗮𝗴𝗻𝗼𝘀𝗲 𝗜𝗺𝗮𝗴𝗲"])

# API KEYS:
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
    
    # Safety Measures for AI
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
    ]

    system_instructions = """

    Use emojies, make it interactive and appealing to the users.
    You are a not actually diagnosing diseases, just deriving to a specific disease based on the symptoms related to it. Avoid saying you are not a medical expert, instead just reference the information below and how you derived to a specific disease from the users input about symptoms. At the end of you response be sure to add “Disease related to symptoms: ‘disease corresponding to symptoms’” for example if all the symptoms provides correlate to HIV, at the end of your response you should have: 
    “Symptoms related to Disease ‘HIV’ or 'Diabetes' or 'STI's'” . 
    Include links to blood labs in South Africa, Kwazulu-Natal for Durban.
    Be motivational and give more information about the disease and its symptoms. 


    Human immunodeficiency virus (HIV) and acquired immunodeficiency syndrome (AIDS)

    Symptoms

    Some people infected by HIV get a flu-like illness within 2 to 4 weeks after the virus enters the body. This stage may last a few days to several weeks. Some people have no symptoms during this stage.
    Possible symptoms include:
    Fever.
    Headache.
    Muscle aches and joint pain.
    Rash.
    Sore throat and painful mouth sores.
    Swollen lymph glands, also called nodes, mainly on the neck.
    Diarrhoea.
    Weight loss.
    Cough.
    Night sweats.
    Diabetes
    Diabetes

    Some of the symptoms of type 1 diabetes and type 2 diabetes are:

    Feeling more thirsty than usual.
    Urinating often.
    Losing weight without trying.
    Presence of ketones in the urine. Ketones are a byproduct of the breakdown of muscle and fat that happens when there's not enough available insulin.
    Feeling tired and weak.
    Feeling irritable or having other mood changes.
    Having blurry vision.
    Having slow-healing sores.
    Getting a lot of infections, such as gum, skin and vaginal infections.
    Sexually transmitted infection (STI’s)
    STI symptoms might include:
    Sores or bumps on the genitals or in the oral or rectal area.
    Painful or burning urination.
    Discharge from the penis.
    Unusual or odorous vaginal discharge.
    Unusual vaginal bleeding.
    Pain during sex.
    Sore, swollen lymph nodes, particularly in the groin but sometimes more widespread.
    Lower abdominal pain.
    Fever.
    Rash over the trunk, hands or feet.

 



"""
    # Initialize the model for text generation
    text_model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instructions
    )

    # Initialize chat session for text generation
    if 'text_chat_session' not in st.session_state:
        st.session_state.text_chat_session = text_model.start_chat(history=[])
        st.session_state.text_chat_history = []

    # This sends prompt to the API using streamlit and generative models .start_chat method
    def generate_text_response(text_input):
        response = st.session_state.text_chat_session.send_message(text_input)
        if response is not None:
            return response.text
        else:
            return "No response available"


    # Text only input:
    text_input = st.chat_input("Enter your text here:", key="text_chat")

    

    # Appends input to API chat history and stores as user role for streamlit 
    if text_input is not None and text_input != "":
        
        st.session_state.text_chat_history.append({
            "role": "user",
            "content": text_input
        })
        # Display chat history 
        st.markdown("### Chat History")
        for chat in st.session_state.text_chat_history:
            st.chat_message(chat["role"]).write(chat["content"])

        # Generates response and stores to chat history as assistant role
        with st.spinner("Generating response..."):
            response = generate_text_response(text_input)
            st.session_state.text_chat_history.append({
                "role": "assistant",
                "content": response
            })

        # Display response
        st.markdown(st.chat_message("assistant" ).write(response))

        # Search for keywords in the entire chat history and decide on button visibility (case-insensitive)
        keywords = ["hiv", "diabetes", "sti's"]
        

            # Display button only if keywords are found in chat history
        if any(keyword in chat["content"].lower() for chat in st.session_state.text_chat_history for keyword in keywords):
            st.link_button("Get Treatment", "http://localhost:8502/")
                # Add functionality to be executed when the button is clicked
        else: 
            pass
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
    
    # Safety Measures for AI
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    system_instructions = """
    

You are a not actually diagnosing diseases, just deriving to a specific disease based on the symptoms related to it. Avoid saying you are not a medical expert, instead just reference the information below and how you derived to a specific disease from the users input about symptoms. At the end of you response be sure to add “Disease related to symptoms: ‘disease corresponding to symptoms’” for example if all the symptoms provides correlate to HIV, at the end of your response you should have: 
    “Symptoms related to Disease ‘HIV’ or 'Diabetes' or 'STI's'” . 
    Include links to blood labs in South Africa, Kwazulu-Natal for Durban.
    Be motivational and give more information about the disease and its symptoms. 


Human immunodeficiency virus (HIV) and acquired immunodeficiency syndrome (AIDS)

Symptoms

Some people infected by HIV get a flu-like illness within 2 to 4 weeks after the virus enters the body. This stage may last a few days to several weeks. Some people have no symptoms during this stage.
Possible symptoms include:
Fever.
Headache.
Muscle aches and joint pain.
Rash.
Sore throat and painful mouth sores.
Swollen lymph glands, also called nodes, mainly on the neck.
Diarrhoea.
Weight loss.
Cough.
Night sweats.
Diabetes
Diabetes

Some of the symptoms of type 1 diabetes and type 2 diabetes are:

Feeling more thirsty than usual.
Urinating often.
Losing weight without trying.
Presence of ketones in the urine. Ketones are a byproduct of the breakdown of muscle and fat that happens when there's not enough available insulin.
Feeling tired and weak.
Feeling irritable or having other mood changes.
Having blurry vision.
Having slow-healing sores.
Getting a lot of infections, such as gum, skin and vaginal infections.
Sexually transmitted infection (STI’s)
STI symptoms might include:
Sores or bumps on the genitals or in the oral or rectal area.
Painful or burning urination.
Discharge from the penis.
Unusual or odorous vaginal discharge.
Unusual vaginal bleeding.
Pain during sex.
Sore, swollen lymph nodes, particularly in the groin but sometimes more widespread.
Lower abdominal pain.
Fever.
Rash over the trunk, hands or feet.

 



"""
    
    # Initialize the model for text generation
    image_model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
        system_instruction=system_instructions
    )

    # Initialize chat session for text generation
    if 'image_chat_session' not in st.session_state:
        st.session_state.image_chat_session = text_model.start_chat(history=[])
        st.session_state.image_chat_history = []

    # This sends prompt to the API about image and returns a response
    def generate_image_response(prompt, image):
        response = image_model.generate_content([prompt, image], stream=True)
        response.resolve()
        return response.text

    # Text and image only input:
    image_text_input = st.chat_input("Enter your text here:", key="image_chat")

    # Image input
    uploaded_image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        bytes_data = uploaded_image.getvalue()
        image = PIL.Image.open(io.BytesIO(bytes_data))
    else:
        image = None


    # Appends input to API chat history and stores as user role for streamlit 
    if image_text_input:
        st.session_state.image_chat_history.append({
            "role": "user",
            "content": image_text_input
        })
        
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Display chat history 
        st.markdown("### Chat History")
        for chat in st.session_state.image_chat_history:
            st.chat_message(chat["role"]).write(chat["content"])
            
        # Generates response and stores to chat history as assistant role
        with st.spinner("Generating response..."):
            response = generate_image_response(image_text_input, image)
            st.session_state.image_chat_history.append({
                "role": "assistant",
                "content": response
            })
        st.markdown(st.chat_message("assistant").write(response))

        # Search for keywords in the entire chat history and decide on button visibility (case-insensitive)
        keywords = ["hiv"]
        show_button = any(keyword in chat["content"].lower() for chat in st.session_state.text_chat_history for keyword in keywords)

        # Display button only if keywords are found in chat history
        if show_button:
            if st.button("Next"):
                # Add functionality to be executed when the button is clicked
                st.write("You clicked the button!")
#----------IMAGE DIAGNOSIS----------
#----------END----------------------


