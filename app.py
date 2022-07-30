from flask import Flask, request, jsonify

# decorators

app = Flask(__name__)

@app.route('/', methods=['GET'])
def echo():
    return 'hello world'