from flask import Flask, request
from flask.json import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def iniciar():
    return "Kevin Joputa"


if __name__ == "__main__":
    app.run(host = "localhost", port = 3000, debug = True)