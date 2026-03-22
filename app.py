from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, flask app is successfully run on jenkins'

@app.route('/health')
def health():
    return 'Server is up and running'
