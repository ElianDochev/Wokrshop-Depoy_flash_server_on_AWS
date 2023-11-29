# create a basic flask app that says hello world on the root route
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)