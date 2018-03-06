from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/person/<name>/<age>')
def name_and_age(name, age):
    return render_template('name_and_age.html', name = name, age = age)

if __name__ == '__main__':
    app.run(debug = True, port = 3000)