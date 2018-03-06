from flask import Flask

app2 = Flask(__name__)

# @app2.route('/add/<int:n1>/<int:n2>')
# def add(n1, n2):
#     return str(n1 + n2)

# @app2.route('/subtract/<int:n1>/<int:n2>')
# def subtract(n1, n2):
#     return str(n1 - n2)

# @app2.route('/multiply/<int:n1>/<int:n2>')
# def multiply(n1, n2):
#     return str(n1 * n2)

# @app2.route('/subtract/<int:n1>/<int:n2>')
# def subtract(n1, n2):
#     return str(n1 - n2)

@app2.route('/math/<string>')
def math(string):
    if(len(string.split('+')) == 2):
        n1 = int(string.split('+')[0])
        n2 = int(string.split('+')[1])
        return str(n1 + n2)
    elif(len(string.split('-')) == 2):
        n1 = int(string.split('-')[0])
        n2 = int(string.split('-')[1])
        return str(n1 - n2)
    if(len(string.split('*')) == 2):
        n1 = int(string.split('*')[0])
        n2 = int(string.split('*')[1])
        return str(n1 * n2)
    if(len(string.split('÷')) == 2):
        n1 = int(string.split('÷')[0])
        n2 = int(string.split('÷')[1])
        return str(n1 / n2)

if __name__ == '__main__':
    app2.run(debug = True, port = 3000)