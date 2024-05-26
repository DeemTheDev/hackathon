from flask import Blueprint, render_template, request, flash, jsonify
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from flask_cors import cross_origin, CORS



auth = Blueprint('auth', __name__)

# Correct CORS configuration
# Allow requests from any origin for '/sign-up' route
# CORS(auth, resources={r"/sign-up": {"origins": "*"}})


@auth.route('/sign-up', methods=['POST', 'OPTIONS'])
# @cross_origin(origin='http://localhost:5173', headers=['Content-Type', 'Authorization'])
def sign_up():
    if request.method == 'OPTIONS':
        response = jsonify({'message': 'Preflight request successful'})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173/sign-up')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'POST', 'OPTIONS')
        return response

    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'message': 'Account already exists with that email address'}), 400
        elif len(email) < 4:
            return jsonify({'message': 'Email must be greater than 4 characters'}), 400

        # elif (len(name) < 2 or len(surname) < 2):
        #         flash('Name must be greater than 1 character', category ='error')
        # # elif (password != password2):
        #     flash('Passwords do not match', category = 'error')

        else:
            # add user to 
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
            new_user = User(email=email, name=name, 
                         password=hashed_password)
            # add to the database
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created!', category='success')
            return jsonify({'message': 'Account Created!', 'user_id': new_user.id}), 201
            
      
   
