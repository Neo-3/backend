from flask import Flask, jsonify


app = Flask(__name__)
app.config["DEBUG"] = True # DEBUG MODE


@app.route("/", methods=["GET"])
def home():
    return "Vou classificar medidor"