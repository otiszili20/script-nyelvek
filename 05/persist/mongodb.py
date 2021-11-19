from pymongo import MongoClient

def get_collection():
    """USERNAME = "root"
    PASSWORD = "example"
    DB_NAME = "sample"
    HOST = "localhost"
    PORT = 27017
    CONNECTION_STRING = f"mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?authSource=admin"""""
    CONNECTION_STRING = "mongodb+srv://OtvosSzilard:example@sample.ps8zo.mongodb.net/labor?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client["myFirstDatabase"]["jobs"]
