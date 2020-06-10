from flask import Flask, jsonify
from api.config import MONGO_URI
import pymongo

# App configurations
app = Flask(__name__)
app.config["DEBUG"] = True  # DEBUG MODE
app.config["MONGO_URI"] = MONGO_URI

client = pymongo.MongoClient(MONGO_URI)
db = client.get_database('Neo3')
