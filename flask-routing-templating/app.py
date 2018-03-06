from flask import Flask, template_rendered, redirect, request, url_for

app = Flask(__name__)

@app.route('/person/<name>/<age>')
def name_and_age(name, age):
    return render_template('name_and_age.html')

if __name__ == '__main__':
    app.run(debug = True, port = 3000)