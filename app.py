from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post', methods=['POST'])
def getVideo():
    content = request.json
    print(content)
    return uuid