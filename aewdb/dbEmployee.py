from datetime import datetime
#from werkzeug.security import generate_password_hash
#from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import db


class Employee(UserMixin, db.Model):
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(25), nullable=False, unique=True)
    pword=db.Column(db.String(16), nullable=False)
    fname=db.Column(db.String(50), nullable=False)
    lname=db.Column(db.String(50), nullable=False)


 #   def set_password(self, password):
 #       self.password_hash = generate_password_hash(password)
#
#    def check_password(self, password):
#        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee{}>'.format(self.username)