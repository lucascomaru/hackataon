from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mdbtreinamentos.db'

database = SQLAlchemy(app)

from mdbtreinamentos import routes