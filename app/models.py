# This file stores our database models
from . import db    # Imports db from the current package
from flask_login import UserMixin
from sqlalchemy.sql import func

class JobHistory(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    job_title = db.Column(db.String(240))
    company = db.Column(db.String(150))
    agency = db.Column(db.String(150))
    date = db.Column(db.String(150))  
    descrip = db.Column(db.String(10000))
    sector = db.Column(db.String(150))

    def __repr__(self):
        return '<Job {}>'.format(self.job_title) 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def __repr__(self):
        return '<User {}>'.format(self.username)