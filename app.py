from flask import Flask
from config import DEBUG

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.config.from_object('config')
print (app.config['DEBUG'])
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
