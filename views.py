from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from . import db
from .models import JobHistory

views = Blueprint("views", __name__)  # Define the blueprint. Name of it is the argument.

@views.route("/")
def home():

    return render_template("home.html", user=current_user)

@views.route("/add_job")
def add_job():

    return render_template("add_job.html", user="admin")