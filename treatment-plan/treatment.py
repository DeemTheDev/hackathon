import pandas as pd
import streamlit as st
from fpdf import FPDF
import json
from streamlit_lottie import st_lottie
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

# Load and prepare the data
treatment_data = pd.read_csv('treatment_plans.csv')

# Encode categorical variables
le_gender = LabelEncoder()
treatment_data['Gender'] = le_gender.fit_transform(treatment_data['Gender'])
le_disease = LabelEncoder()
treatment_data['Disease'] = le_disease.fit_transform(treatment_data['Disease'])

# Ensure no missing values
treatment_data.fillna(0, inplace=True)

# Select features and target
X = treatment_data[['Disease', 'Age', 'Gender']]
y = treatment_data[['Medication', 'Dosage', 'Prevention', 'Diet']]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Function to get treatment plan
def get_treatment_plan(disease, age, gender, symptoms):
    disease_encoded = le_disease.transform([disease])[0]
    gender_encoded = le_gender.transform([gender])[0]
    input_data = [[disease_encoded, age, gender_encoded]]
    prediction = model.predict(input_data)
    plan = {
        'Disease': disease,
        'Medication': prediction[0][0],
        'Dosage': prediction[0][1],
        'Prevention': prediction[0][2],
        'Diet': prediction[0][3]
    }
    return plan

# Function to generate PDF
def generate_pdf(plan, patient_name, date, symptoms):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Set header color to teal
    pdf.set_fill_color(72, 209, 204)
    pdf.rect(0, 0, 210, 40, 'F')
    
    # Set logo in the corner
    pdf.image("assets/ai header.jpg", x=160, y=8, w=40)
    
    pdf.set_text_color(0, 0, 0)  # Black color for text
    
    pdf.cell(200, 10, txt="DR AI: YOUR CUSTOMIZED TREATMENT PLAN", ln=True, align='C')
    pdf.cell(200, 10, txt=f"PATIENT NAME: {patient_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"DATE: {date}", ln=True, align='L')
    pdf.cell(200, 10, txt="\n", ln=True, align='L')
    pdf.cell(200, 10, txt="TREATMENT PLAN:", ln=True, align='L')
    for key, value in plan.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
    pdf.cell(200, 10, txt="\n", ln=True, align='L')
    pdf.cell(200, 10, txt="DIET PLAN:", ln=True, align='L')
    pdf.cell(200, 10, txt="1. Eat a balanced diet rich in fruits, vegetables, and lean proteins.", ln=True, align='L')
    pdf.cell(200, 10, txt="2. Limit intake of sugar and processed foods.", ln=True, align='L')
    pdf.cell(200, 10, txt="3. Monitor carbohydrate intake and follow a consistent meal schedule.", ln=True, align='L')
    pdf.cell(200, 10, txt=" Eat regular meals and snacks to prevent blood sugar spikes and drops.", ln=True, align='L')
    pdf.cell(200, 10, txt="\n", ln=True, align='L')
    pdf.cell(200, 10, txt="EXERCISE PLAN:", ln=True, align='L')
    pdf.cell(200, 10, txt="1. Engage in moderate aerobic exercise for at least 30 minutes a day, 5 days a week.", ln=True, align='L')
    pdf.cell(200, 10, txt="2. Incorporate strength training exercises 2-3 times a week.", ln=True, align='L')
    pdf.cell(200, 10, txt="3. Consult with a healthcare provider before starting any new exercise regimen.", ln=True, align='L')
    pdf.cell(200, 10, txt="\n", ln=True, align='L')
    pdf.cell(200, 10, txt="YOUR SYMPTOMS:", ln=True, align='L')
    for symptom in symptoms:
        pdf.cell(200, 10, txt=f"- {symptom}", ln=True, align='L')
    return pdf.output(dest='S').encode('latin1')

# Streamlit UI
st.title('DR AI')

st.sidebar.title('DR AI: HOW CAN I HELP')
disease_names = le_disease.classes_
disease = st.sidebar.selectbox('SELECT DISEASE', disease_names)
age = st.sidebar.number_input('AGE', min_value=0, max_value=120, value=30)
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
#Animation
left_column, right_column = st.columns(2)

with left_column:
    st.header("""
                  
            Treatment Plan 
                  
        """)

with right_column:
    with open("./assets/animation-d.json", "r") as a:
        animation = json.load(a)
    st_lottie(animation, quality='high', height=200)

# Fetch symptoms for the selected disease from the dataframe
symptoms = treatment_data.loc[treatment_data['Disease'] == le_disease.transform([disease])[0], 'Symptoms'].iloc[0].split(', ')
symptoms.extend(treatment_data.loc[treatment_data['Disease'] == le_disease.transform([disease])[0], 'Additional_Symptoms'].iloc[0].split(', '))

# Display the fetched symptoms in the multiselect widget
selected_symptoms = st.sidebar.multiselect('Select Symptoms', symptoms)

patient_name = st.sidebar.text_input('PATIENT NAME:')
date = datetime.now().strftime("%Y-%m-%d")

if st.sidebar.button('VIEW TREATMENT PLAN'):
    if not selected_symptoms:
        st.error("PLEASE SELECT AT LEAST ONE SYMPTOM.")
    else:
        plan = get_treatment_plan(disease, age, gender, selected_symptoms)
        st.subheader('Treatment Plan Details:')
        st.markdown("### TREATMENT PLAN")
        st.write(f"Disease: {plan['Disease']}")
        st.write(f"Medication: {plan['Medication']}")
        st.write(f"Dosage: {plan['Dosage']}")
        st.write(f"Prevention: {plan['Prevention']}")
        st.write(f"Diet: {plan['Diet']}")
        st.markdown("### DIET PLAN")
        st.write("1. Eat a balanced diet rich in fruits, vegetables, and lean proteins.")
        st.write("2. Limit intake of sugar and processed foods.")
        st.write("3. Monitor carbohydrate intake and follow a consistent meal schedule.")
        st.markdown("### EXERCISE PLAN")
        st.write("1. Engage in moderate aerobic exercise for at least 30 minutes a day, 5 days a week.")
        st.write("2. Incorporate strength training exercises 2-3 times a week.")
        st.write("3. Consult with a healthcare provider before starting any new exercise regimen.")

        pdf_bytes = generate_pdf(plan, patient_name, date, selected_symptoms)
        st.download_button(label='Download Treatment Plan PDF', data=pdf_bytes, file_name='treatment_plan.pdf', mime='application/pdf')

# Display statistics
st.sidebar.title('DISEASE STATS')
stats = {
    'HIV': 37,
    'TB': 25,
    'Diabetes': 10
}
for disease, percent in stats.items():
    st.sidebar.write(f"{disease}: {percent}%")
    st.sidebar.progress(percent / 100)
