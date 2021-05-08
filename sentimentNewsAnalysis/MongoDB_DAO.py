from pymongo import MongoClient


class MongoDB_DAO:
    def __init__(self, database_name):
        print("MONGODB DATABASE CONNECTION ESTABLISHMENT ...")
        self.client = MongoClient('mongodb+srv://[Username]:[Password]@[MongoDB cluster repo]/')
        self.database = self.client[database_name]

    def collections_list(self):
        return self.database.list_collection_names()

    def retrieve_data(self, collection_name):
        print("Retrieve data from database ...")
        collection = self.database[collection_name]
        document_retrieved = collection.find()
        return document_retrieved

    def retrieve_tweets(self, collection_name):
        print("Retrieve tweets from database ...")
        collection = self.database[collection_name]
        tweet_retrieved = collection.find()
        return tweet_retrieved

    def save_data(self, record, collection_name):
        print("Save data in database...")
        collection = self.database[collection_name]
        collection.insert_one(record)

    def save_multiple_records(self, list_of_tweets, collection_name):
        print("Save multiple records in database...")
        collection = self.database[collection_name]
        collection.insert_many(list_of_tweets)

    def close_connection(self):
        self.database.close()
