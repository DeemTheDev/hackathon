from flask import Flask, render_template, request, jsonify
from chatbot.chat import get_Response
from Backend.__init__ import create_app
from flask_cors import CORS
from flask_login import current_user, login_required

app = create_app()

@app.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return current_user


@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_Response(text)
    message = {'answer': response}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)