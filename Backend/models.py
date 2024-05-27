from .__init__ import db
from flask_login import UserMixin #helps login users
from sqlalchemy.sql import func #allows use of SQL functions like datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    # surname = db.Column(db.String(150))
    # notes = db.relationship('Note')
    # n:n relationship between user and groups 
    # allows users to be part of multiple groups
    # and groups to have multiple users
