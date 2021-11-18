from flask import Flask
from calculator_router import calculator_api

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


if __name__ == '__main__':
    print(f'Hello World')
    app.register_blueprint(calculator_api)
    app.run(host='0.0.0.0', port=5001, debug=True)
