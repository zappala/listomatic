from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# generate with os.urandom(24) in a Python shell
SECRET_KEY = ''
# get these by registering an app with Twitter
TWITTER_KEY = ''
TWITTER_SECRET = ''

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
db = SQLAlchemy(app)

from models.user import *
from models.item import *

db.create_all()
