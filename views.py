"""
Routes and views for the flask application.
"""

from datetime import datetime
import html
from flask import render_template, Blueprint, request, flash, redirect, url_for, session
from passlib.hash import sha256_crypt
#from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm


views=Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

