from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# handle sessions for each user that is logged in 
login_manager = LoginManager(app)

# we access it based on the method route
# declare route /login to be implemented on routes.py above the /account route
login_manager.login_view = 'login'
# just bootstrap class for flask
login_manager.login_message_category = 'info'

from flaskblog import routes