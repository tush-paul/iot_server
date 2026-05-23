from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Connection
MONGO_URI = "mongodb+srv://tusharadri123_db_user:Nur23hxV8s7g6NNO@cluster0.k4kjemp.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client.iot_database

collection = db.sensor_data

@app.route('/')
def home():
    return "IoT Server Running"

@app.route('/data', methods=['POST'])
def receive_data():

    data = request.json

    # Add timestamp
    data["timestamp"] = datetime.utcnow()

    # Store in MongoDB
    collection.insert_one(data)

    print("Stored:", data)

    return {
        "status": "success"
    }

@app.route('/view')
def view():

    data = list(
        collection.find({}, {"_id": 0})
    )

    return data

if __name__ == "__main__":
    app.run()
