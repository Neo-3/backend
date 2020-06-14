from flask import Flask, jsonify
from api.config import MONGO_URI
from mongoengine import connect
from api import models

# App configurations
app = Flask(__name__)
app.config["DEBUG"] = True  # DEBUG MODE
app.config["MONGO_URI"] = MONGO_URI

# Stabilish a connection with mongoDB
connect(host=MONGO_URI)