from flask import Flask, jsonify, request
from mongoengine import connect
from decouple import config
from api import models

# Envoiroment variables
MONGO_URI = config("MONGO_URI")

# App configurations 
app = Flask(__name__)
app.config["DEBUG"] = True  # DEBUG MODE
app.config["MONGO_URI"] = MONGO_URI

# Stabilish a connection with mongoDB
connect(host=MONGO_URI, db='models') 
