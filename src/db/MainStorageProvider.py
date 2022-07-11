from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

import urllib.parse
import config

from bson.objectid import ObjectId
from bson import json_util

from typing import Dict, List


class MainStorageProvider:
    def __init__(self):
        self._username = urllib.parse.quote_plus(config.db.USERNAME)
        self._password = urllib.parse.quote_plus(config.db.PASSWORD)

        self._client = self._connect()
        self._db = self._client[config.db.DATABASE_NAME]

        if config.db.COLLECTION_NAME not in self._db.list_collection_names():
            self._client.cluster0.create_collection(config.db.COLLECTION_NAME)
        #

        self._collection = self._db[config.db.COLLECTION_NAME]

    #

    def _connect(self):
        try:
            client = MongoClient(
                f"mongodb+srv://{self._username}:{self._password}@{config.db.DATABASE_NAME}.bauczka.mongodb.net/?retryWrites=true&w=majority",
                server_api=ServerApi("1"),
                socketTimeoutMS=7000,
                connectTimeoutMS=7000,
            )

            client.admin.command("ismaster")
            return client

        except ConnectionFailure:
            raise Exception("server not available")
        #

    #

    def save(self, data: Dict):
        if "_id" in data.keys() and data["_keys"]:
            try:
                self._collection.update_one(data)
                return
            except Exception as e:
                raise Exception(
                    f"error trying to update existing object in databse: {data}"
                )
        #

        try:
            self._collection.insert_one(data)
        except Exception as e:
            raise Exception(f"error trying to save new object in database: {data}")

    #

    def saveAll(self, data: List[Dict]) -> None:
        for document in data:
            self.save(document)
        #

    #

    def get(self, id):
        return json_util.dumps(self._collection.find_one({"_id": ObjectId(id)}))

    #

    def getAll(self):
        return self._collection.find({})

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

    def close(self):
        self._client.close()

    #


#
