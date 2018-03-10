from flask import Flask, redirect, request, render_template, url_for, jsonify
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/bootcamps-app'
app.config['SQLALCHEMY_ECHO'] = True
modus = Modus(app)
db = SQLAlchemy(app)

class Bootcamp(db.Model):

    __tablename__ = 'bootcamps'
    # DDL
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    votes = db.Column(db.Integer)

    #DML
    def __init__(self, name, location, votes):
        self.name = name
        self.location = location
        self.votes = votes

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/bootcamps')
def index():
    return render_template('index.html', bootcamps = Bootcamp.query.all())
