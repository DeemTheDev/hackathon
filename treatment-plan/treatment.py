# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
import json
from streamlit_lottie import st_lottie
from fpdf import FPDF
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder


# Load and prepare the data
treatment_data = pd.read_csv('./treatment_plans.csv')

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
model.fit(X_train.values, y_train)

# Function to get treatment plan
def get_treatment_plan(disease, age, gender):
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
def generate_pdf(plan):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Treatment Plan", ln=True, align='C')
    for key, value in plan.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
    return pdf.output(dest='S').encode('latin1')

# Streamlit UI
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


st.sidebar.title('User Inputs')

#Choose disease from Disease Diagnosis


# Import the diagnosis module
from diagnosis import get_disease_options

# Get disease options
disease_options = get_disease_options()

disease  = st.sidebar.selectbox('Select Disease', disease_options)
age = st.sidebar.number_input('Age', min_value=0, max_value=120, value=30)
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
symptoms = st.sidebar.text_area('Symptoms (optional)')

if st.sidebar.button('View Treatment Plan'):
    plan = get_treatment_plan(disease, age, gender)
    st.subheader('Treatment Plan Details:')
    st.write(f"Disease: {plan['Disease']}")
    st.write(f"Medication: {plan['Medication']}")
    st.write(f"Dosage: {plan['Dosage']}")
    st.write(f"Prevention: {plan['Prevention']}")
    st.write(f"Diet: {plan['Diet']}")

    pdf_bytes = generate_pdf(plan)
    st.download_button(label='Download Treatment Plan as PDF', data=pdf_bytes, file_name='treatment_plan.pdf', mime='application/pdf',)

# Display statistics
st.sidebar.title('Disease Statistics')
stats = {
    'HIV': 37,
    'TB': 25,
    'Diabetes': 10
}
for disease, percent in stats.items():
    st.sidebar.write(f"{disease}: {percent}%")
    st.sidebar.progress(percent / 100)