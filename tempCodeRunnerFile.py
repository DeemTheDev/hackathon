from flask import Flask, render_template, request, jsonify
from chatbot.chat import get_Response


app = Flask(__name__, template_folder='chatbot/templates')


@app.post('/predict')
def predict():
    text = request.get_json().get('message')
    response = get_Response(text)
    message = {'answer': response}
    return jsonify(message)



if __name__ == '__main__':
    app.run(debug=True)