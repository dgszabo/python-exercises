from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/mondays'
app.config['SQLALCHEMY_ECHO'] = True

# this is practically connecting us to the ORM
db = SQLAlchemy(app)
Migrate(app, db)

class Day(db.Model):

    __tablename__ = 'days'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    mood = db.Column(db.Text)
    weather = db.Column(db.Text)
    events_happenning = db.Column(db.Boolean, nullable = False, default = False)


