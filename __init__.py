from flask import Flask
from pymongo import MongoClient
import bcrypt

# Initialize the app
app = Flask(__name__)

# Load configurations from config.py
app.config.from_object('config.Config')

# MongoDB connection
client = MongoClient(app.config['MONGO_URI'])
db = client[app.config['MONGO_DBNAME']]

# Import routes to register them with the Flask app
from app import routes
