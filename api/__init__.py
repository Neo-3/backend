from flask import Flask, jsonify, request
from api.config import MONGO_URI
import pymongo
import os

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '/uploads')

# App configurations
app = Flask(__name__)
app.config["DEBUG"] = True  # DEBUG MODE
app.config["MONGO_URI"] = MONGO_URI
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = pymongo.MongoClient(MONGO_URI)
db = client.get_database('Neo3')
