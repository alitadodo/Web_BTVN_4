from pymongo import MongoClient
mongo_uri = "mongodb+srv://admin:admin@c4e28-cluster-725hk.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
service_database = client.db_service
services = service_database["bike"]