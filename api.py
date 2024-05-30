from flask import request, jsonify
from chatbot.chat import get_Response
from database.__init__ import create_app
from flask_cors import CORS

app = create_app()

# Decorator to define a route for POST requests to '/predict'
@app.post('/predict')  
def predict(): 
    # Extract the text message from the JSON payload of the request
    text = request.get_json().get('message')

    # Call a function to get a response based on the input text
    response = get_Response(text)

    # Create a dictionary containing the response message
    message = {'answer': response}

    # Convert the dictionary into a JSON response and return it
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
    