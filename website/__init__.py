from flask import Flask
from os import path
from pymongo import MongoClient
from mongoengine import *


DB_NAME = "database.db"

def create_app():
    
    app = Flask(__name__)
    
    
    from .views import views

    app.register_blueprint(views,url_prefix="/")

    client = MongoClient(host = 'test_mongodb',
                    port=27017,
                    username='root',
                    password='password',
                    authSource="admin")
    db = client.nlp_analysis
    db.register
    
    # from .models import Inputtext
    # create_db(app)

    return app

# def create_database(app):f
#     if not path.exists("website/" + DB_NAME):
#         db.create_all(app=app)
#         print("created database")

def create_db():
    client = MongoClient(host = 'test_mongodb',
                    port=27017,
                    username='root',
                    password='password',
                    authSource="admin")
    db = client.nlp_analysis
    records = db.register
    return records