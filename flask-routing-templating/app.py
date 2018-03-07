from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/person/<name>/<age>')
def name_and_age(name, age):
    return render_template('name_and_age.html', name = name, age = age)

@app.route('/calculator')
def calculator():
    return render_template('calculator.html') 

@app.route('/math')
def math():
    n1 = float(request.args.get('first_number'))
    n2 = float(request.args.get('second_number'))
    operation = request.args.get('operation')
    if(operation == 'add'):
        return str(n1 + n2)
    elif(operation == 'subtract'):
        return str(n1 - n2)
    if(operation == 'multiply'):
        return str(n1 * n2)
    if(operation == 'divide'):
        return str(n1 / n2)

if __name__ == '__main__':
    app.run(debug = True, port = 3000)