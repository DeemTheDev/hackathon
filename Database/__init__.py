from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "database.db"

def create_database(app):
    db_path = path.join(app.instance_path, DB_NAME)
    if not path.exists(db_path):
        with app.app_context():
            db.create_all()
            print('Created Database!')
    else:
        print('Database already exists!')

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'dalziel'

    # Set up the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"

    # Ensure that the SQLAlchemy instance is properly initialized with the app
    db.init_app(app)

    # Access the database engine within the application context
    with app.app_context():
        # Check if the SQLAlchemy engine is initialized
        if db.engine is not None:
            print("Flask app is connected to the database.")
        else:
            print("Flask app is NOT connected to the database.")

    # Import blueprints and models within the function scope to avoid circular imports
    from .auth import auth
    

    # Register blueprints
    app.register_blueprint(auth, url_prefix='/auth')

    from .models import User
    
    # Create the database if it doesn't exist
    create_database(app)
    return app
