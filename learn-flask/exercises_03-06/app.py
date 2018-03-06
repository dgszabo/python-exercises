from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def wc1():
    return 'welcome'

@app.route('/welcome/home')
def wc2():
    return 'welcome home'

@app.route('/welcome/back')
def wc3():
    return 'welcome back'

@app.route('/sum')
def sum():
    sum = 5 + 5
    return str(sum)

if __name__ == '__main__':
    app.run(debug = True, port = 3000)