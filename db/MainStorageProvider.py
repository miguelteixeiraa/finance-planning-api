from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
import urllib.parse
import db.config as config
from bson import json_util
from bson.objectid import ObjectId
from typing import Dict, List


class MainStorageProvider:
    def __init__(self):
        self._username = urllib.parse.quote_plus(config.USERNAME)
        self._password = urllib.parse.quote_plus(config.PASSWORD)

        self._client = self._connect()
        self._db = self._client[config.DATABASE_NAME]

        if config.COLLECTION_NAME not in self._db.list_collection_names():
            self._client.cluster0.create_collection(config.COLLECTION_NAME)
        #

        self._collection = self._db[config.COLLECTION_NAME]

    #

    def _connect(self):
        try:
            client = MongoClient(
                f"mongodb+srv://{self._username}:{self._password}@{config.DATABASE_NAME}.bauczka.mongodb.net/?retryWrites=true&w=majority",
                server_api=ServerApi("1"),
            )
            client.admin.command("ismaster")
            return client

        except ConnectionFailure:
            raise Exception("Server not available")
        #

    #

    def save(self, data: Dict):
        if "_id" in data.keys() and data["_keys"]:
            self._collection.update_one(data)
            return
        #

        self._collection.insert_one(data)

    #

    def saveAll(self, data: List[Dict]):
        for document in data:
            self.save(document)
        #

    #

    def get(self, id):
        return json_util.dumps(self._collection.find_one({"_id": ObjectId(id)}))

    #

    def getAll(self):
        return json_util.dumps(self._collection.find({}))

    #

    def delete(self, id):
        self._collection.delete_one({"_id": ObjectId(id)})
        return

    #

    def deleteAll(self, query: Dict):
        self._collection.delete_many(query)

    #

    def deleteAll(self):
        self._collection.delete_many({})

    #


#
