from flask import Blueprint, render_template, request, flash, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .__init__ import db
from flask import redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from flask_cors import cross_origin, CORS
import re


auth = Blueprint('auth', __name__)


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
        password = data.get('password')


        # password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'Account already exists with that email address'}), 400
        
        elif len(email) < 4 or not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return jsonify({'message': 'Please enter a valid email address'}), 400

        elif len(username) < 6 :
               return jsonify({'message':'Username must be at least 6 characters long '}), 400
        
        else:
            # add user to 
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(email=email, name=username, password=hashed_password)
            # add to the database
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            return jsonify({'message': 'Account Created!', 'user_id': new_user.id}), 201


            
      
   
