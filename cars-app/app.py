from flask import Flask, render_template, url_for, redirect, request
from flask_modus import Modus
from car import Car

cars = [Car("Toyota", "Corolla", 2005), Car("Toyota", "Corolla S", 2005)]

app = Flask(__name__)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/cars')
def index():
    return render_template('index.html', cars=cars)

@app.route('/cars/new')
def new():
    return render_template('new.html')

@app.route('/cars', methods = ['POST'])
def create():
    # get some data via POST request (almost request.args)
    make = request.form.get('make')
    model = request.form.get('model')
    year = request.form.get('year')
    return redirect(url_for('index'))

# @app.route("/cars", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         # get some data from a form
#     return render_template("index.html", cars=cars)

if __name__ == '__main__':
    app.run(debug = True, port = 3000)