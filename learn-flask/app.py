from flask import Flask

app = Flask(__name__)

# listen for HTTP requests to '/'
# 1 - specify the route and HTTP verb
@app.route('/')
# 2 - define a function to be run, when that route is reached
def route():
    return 'Hello World!'

@app.route('/rithm')
def say_hi():
    return 'Hello class!'

@app.route('/instructor/<name>')
def hi_instructor(name):
    return f'Hello {name}!'

if __name__ == '__main__':
    app.run(debug=True, port=3000)