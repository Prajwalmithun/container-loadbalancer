from flask import request, Flask
import json

app1 = Flask(__name__)
@app1.route('/')

def hello_dude():
    return("Hi, welcome to App2")

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')