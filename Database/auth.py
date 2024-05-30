from flask import Blueprint,request, jsonify
from .models import User
from werkzeug.security import generate_password_hash
from .__init__ import db
import re

auth = Blueprint('auth', __name__)

# Decorator to define a route for POST requests to '/sign-up'
@auth.post('/sign-up')
def sign_up():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST', 'OPTIONS')
        return response

    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'Account already exists with that email address'}), 400
        
        elif len(email) < 4 or not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return jsonify({'message': 'Please enter a valid email'}), 400

        elif len(username) < 6 :
               return jsonify({'message':'Username must be at least 6 characters long '}), 400
        
        else:
            # add user to 
            new_user = User(email=email, name=username)

            # add to the database
            db.session.add(new_user)
            db.session.commit()

            # login_user(user, remember=True)
            return jsonify({'message': 'Account Created!', 'user_id': new_user.id}), 201


            
      
   
