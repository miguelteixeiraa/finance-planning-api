from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

import dbConfig

from bson.objectid import ObjectId
from bson import json_util

from typing import Dict, List


class MockMainStorageProvider:
    def __init__(self):
        pass

    #

    def save(self, data: Dict):
        pass

    #

    def saveAll(self, data: List[Dict]) -> None:
        pass

    #

    def get(self, id):
        pass

    #

    def getAll(self):
        pass

    #

    def delete(self, id):
        pass

    #

    def deleteAll(self, query: Dict):
        pass

    #

    def deleteAll(self):
        pass

    #

    def close(self):
        pass

    #


#
