from flask import Flask, render_template, request, jsonify
from chatbot.chat import get_Response
from flask_cors import CORS
import test



app = Flask(__name__, template_folder='chatbot/templates')
CORS(app)

@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_Response(text)
    message = {'answer': response}
    return jsonify(message)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #Get user data from request 
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    #Call database function:
    try:
        db_response = test.get_api(username, email, password)
        if db_response: #Check if function was successful 
            return jsonify({"message": "Account created successfully"}), 201
        else:
            return jsonify({"message": "Account creation failed"}), 500
    except Exception as e:
        print(e)
        return jsonify({"message": "An error occurred"}), 201





if __name__ == '__main__':
    app.run(debug=True)
    