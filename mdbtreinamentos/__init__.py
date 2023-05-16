from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mdbtreinamentos.db'

database = SQLAlchemy(app)

app.config['SECRET_KEY'] = '3f98e2371e99bb70b79c4129bbae780d'

from mdbtreinamentos import routes