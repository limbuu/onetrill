from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, New 7yw7yf7y7ysysd World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
