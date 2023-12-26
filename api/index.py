from flask import Flask
app = Flask(__name__)

@app.route("/api/python", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"
