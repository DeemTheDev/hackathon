from flask import Flask, render_template, request, jsonify
from chatbot.chat import get_Response
from flask_cors import CORS
import subprocess

#RUN THE BACKEND FILES WITH THIS CODE:

#THIS FUNCTION AUTOMATICALLY RUNS ALL THE BACKEND PYTHON FILES. 
def run_backend():
    #Run disease diagnosis FILE:
    st_diseaseDiagnosis = subprocess.Popen(['streamlit', 'run', 'diagnosis.py', '--server.port', '8501', '--server.headless', 'true'], cwd='disease-diagnosis/')
    st_diseaseDiagnosis.wait()

app = Flask(__name__, template_folder='chatbot/templates')
CORS(app)

@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_Response(text)
    message = {'answer': response}
    return jsonify(message)



if __name__ == '__main__':
    
    app.run(debug=True)
    run_backend()