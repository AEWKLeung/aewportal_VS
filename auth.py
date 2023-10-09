from flask import Blueprint, render_template
#from flask_login import login_user, logout_user, login_required, current_user
#from flask_wtf import FlaskForm
#from wtforms import BooleanField, StringField, PasswordField, validators
#from werkzeug.security import generate_password_hash, check_password_hash
#from passlib.hash import sha256_crypt

#from . import db

auth=Blueprint('auth', __name__)

@auth.route('register',methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@auth.route('login',methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('about')
def about():
    return render_template('about.html')