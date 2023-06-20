from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = '8793fb69e50e9558a12a8aa6b548d52880f2290b'
app.config["MONGO_URI"] = "mongodb+srv://khalil:YchPOJXzKBjMPOZI@cluster0.0azwkml.mongodb.net/myDB?retryWrites=true&w=majority"
#setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes
