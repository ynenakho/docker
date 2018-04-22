from flask import Flask
app = Flask("test_app")

@app.route('/')
def hello_world():
    return 'Hello, World!'
