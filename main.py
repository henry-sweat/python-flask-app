# import flask
from flask import Flask

# initialize app variable
app = Flask(__name__)

# route requests with the stated URL string to run the below the function
@app.route("/")
def hello():
    return "Hello World!"

# run app
if __name__ == "__main__":
    app.run()
