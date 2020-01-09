from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/summary')
def summary():
    # data = {"error": "Invalid email", "code": "INVALID_EMAIL"}
    # response = app.response_class(
    #     response=data,
    #     status=200,
    #     mimetype='application/json'
    # )
    # return response
    return {"error": "Invalid email", "code": "INVALID_EMAIL"}, 200

if __name__ == '__main__':
    app.run(debug=True)