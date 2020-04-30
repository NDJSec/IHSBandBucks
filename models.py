from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):

    __tablename__= "users"

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.String(100), unique=True, nullable=False)
    password = db.Column('password', db.String(100), unique=True, nullable=False)
    name = db.Column('name', db.String(1000), nullable=False)
    amount = db.Column('amount', db.Integer, nullable=False, default=0)

    def __init__(self, id, email, password, name, amount):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.amount = amount
