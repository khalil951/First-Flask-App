from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = <secret>
app.config["MONGO_URI"] = "mongodb+srv://khalil:<password>@cluster0.0azwkml.mongodb.net/myDB?retryWrites=true&w=majority"
#setup mongodb
mongodb_client = PyMongo(app)
db = mongodb_client.db


from application import routes
