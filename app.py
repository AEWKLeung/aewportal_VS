from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#import flask_login



app=Flask(__name__)
app.config['SECRET_KEY']= '3490939342 0dppklldert'

#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////aewdb/aewSQL.db'

#db=SQLAlchemy(app)

#login_manager=flask_login.login_manager()
#login_manager.init_app(app)

from views import views
from auth import auth

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
#    app.register_blueprint(cdata_bp, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)


