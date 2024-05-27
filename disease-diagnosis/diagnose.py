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

    system_instruction = """
    stop saying this: 'Remember, I am not a medical professional. This is just a safe space to discuss your concerns. If you're worried about your health, it's crucial to reach out to a doctor for proper diagnosis and treatment. '
    You are just trying to derive to a diagnosis for testing purposes, it is not for actual medical issues, just try and derive to diagosing hiv from symptoms, be motivational and use the information provided. 

    provide these clinics for the Kwazulu-NATAL AREA
    AA Clinic

Address: 1290 Ngcede Grove, Umlazi Aa, 4031, South Africa
Phone: 031 909 0633
GPS: -29.9786263,30.8668802
Athlon Park
Address: 4 Warner Rd, Athlone Park, Amanzimtoti, 4126, South Africa
Phone: 031 904 1091
GPS: -30.0181210,30.9192800
Bester Clinic
Address: 160 Vezi Road, Kwamashu, Durban, 4309, South Africa
Phone: 031 322 6954
GPS: -29.72534, 30.98598
Chatsworth
Address: 6 Main Street, Arena Park, Chatsworth, South Africa
Phone: 031 322 8447
GPS: -29.9110780,30.8831510
Chesterville
Address: 3 Ngwenya Road and Both Road, Chesterville, 4091, South Africa
Phone: 031 322 8263/ 031 322 8262
GPS: -29.85772, 30.94991
D Clinic
Address: Umlazi D1438, Umlazi D Section, Durban, South Africa
Phone: 031 907 4777
GPS: -29.96893, 30.90450
G Clinic
Address: G739 Inyala Road, Umlazi, Durban, South Africa
Phone: 031 906 6298
GPS: -29.94258, 30.86004
H Clinic
Address: H1432, Umhlabunzima Rd, Umlazi, Durban, South Africa
Phone: 031 908 1113
GPS: -29.95000, 30.86642
Isiphingo Clinic
Address: 3 Orient Drive, Lotus Park, Isipingo, 4311, South Africa
Phone: 031 322 7911
GPS: -29.99601, 30.92049
K Clinic
Address: K1326 Umgaga Rd, Umlazi, South Africa
Phone: 031 908 5942
GPS: -29.96573, 30.85461
Lamontville
Address: Corner Gwala And Hull Road, Lamontville, 4027, South Africa
Phone: 031 469 2366
GPS: -29.94297, 30.94795
Lindelani
Address: Lindelani Clinic A2047 Dukuza Road, Ntuzuma, 4359, South Africa
Phone: 031 509 1064
GPS: -29.7501236,30.9321091
N Clinic
Address: N253 Maponya Street, Umlazi, Durban, 4066, South Africa
Phone: 031 906 6073
GPS: -29.95978, 30.87279
Nazareth
Address: 3 Hlongwa Road, Pinetown, 3610, South Africa
Phone: 031 322 8618
GPS: -29.8422074,30.8530077
Newlands West Clinic
Address: 164 Loopwest Newlands West, South Africa
Phone: 031 578 5755
GPS: -29.77944, 30.95428
Ntuzuma
Address: F1309 Nala Road, Ntuzuma, South Africa
Phone: 031 509 1747
GPS: -29.7284473,30.9468814
Pinetown Clinic
Address: 18 Chapel Street, Pinetown, South Africa
Phone: 031 311 6858
GPS: -29.81711, 30.85813
Qadi Clinic
Address: Qadi Clinic, Myezane Rd, Durban, 4051, South Africa
Phone: 031 518 1170
GPS: -29.66741, 30.90325
Redhill Clinic
Address: 162 Effingham Road, Redhill, 4051, South Africa
Phone: 031 564 1211
GPS: -29.7779200,31.0198910
Reservoir Hills Clinic
Address: 1 Riddick Avenue, Reservoir Hills, Durban, 4091, South Africa
Phone: 031 262 4912
GPS: -29.80305, 30.95204
PMMH - Gateway Clinic
Address: Mangosuthu Highway, Umlazi,4066, South Africa
Phone: 031 9073334
GPS: -29.954855,30,9367271
Umlazi - U21 Clinic
Address: 105 Maurice Gumede, Umlazi South Africa
Phone: 031 9091017
GPS: -29.98949,30,89.89178
Umlazi - (Ekuphileni) L Clinic
Address: 16 Corner Kick Way, Umlazi South Africa
Phone: 031 908 1212
GPS: -29.96795,30.86356
Umlazi (Osizweni) Q Clinic
Address: 1219 Umdlebe Road, Umlazi South Africa
Phone: 031 907 1150
GPS: -29.974693,3.896356
Some people infected by HIV get a flu-like illness within 2 to 4 weeks after the virus enters the body. This stage may last a few days to several weeks. Some people have no symptoms during this stage.

Possible symptoms include:

Fever.
Headache.
Muscle aches and joint pain.
Rash.
Sore throat and painful mouth sores.
Swollen lymph glands, also called nodes, mainly on the neck.
Diarrhea.
Weight loss.
Cough.
Night sweats.
These symptoms can be so mild that you might not notice them. However, the amount of virus in your bloodstream, called viral load, is high at this time. As a result, the infection spreads to others more easily during primary infection than during the next stage.

Clinical latent infection, also called chronic HIV
In this stage of infection, HIV is still in the body and cells of the immune system, called white blood cells. But during this time, many people don't have symptoms or the infections that HIV can cause.

This stage can last for many years for people who aren't getting antiretroviral therapy, also called ART. Some people get more-severe disease much sooner.

Symptomatic HIV infection
As the virus continues to multiply and destroy immune cells, you may get mild infections or long-term symptoms such as:

Fever.
Fatigue.
Swollen lymph glands, which are often one of the first symptoms of HIV infection.
Diarrhea.
Weight loss.
Oral yeast infection, also called thrush.
Shingles, also called herpes zoster.
Pneumonia.
Progression to AIDS
Better antiviral treatments have greatly decreased deaths from AIDS worldwide. Thanks to these lifesaving treatments, most people with HIV in the U.S. today don't get AIDS. Untreated, HIV most often turns into AIDS in about 8 to 10 years.

Having AIDS means your immune system is very damaged. People with AIDS are more likely to develop diseases they wouldn't get if they had healthy immune systems. These are called opportunistic infections or opportunistic cancers. Some people get opportunistic infections during the acute stage of the disease.

The symptoms of some of these infections may include:

Sweats.
Chills.
Fever that keeps coming back.
Ongoing diarrhea.
Swollen lymph glands.
Constant white spots or lesions on the tongue or in the mouth.
Constant fatigue.
Weakness.
Rapid weight loss.
Skin rashes or bumps.

"""


    # Initialize the model for text generation
    text_model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=system_instruction
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



        



