from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/mondays'
app.config['SQLALCHEMY_ECHO'] = True

# this is practically connecting us to the ORM
db = SQLAlchemy(app) 

class Day(db.Model):

    __tablename__ = 'days'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name


