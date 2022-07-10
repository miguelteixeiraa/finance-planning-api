from MainStorageProvider import MainStorageProvider
from typing import Dict
from bson import ObjectId, json_util
from Type import Type


class TypeService:
    def __init__(self) -> None:
        self._typesCollectionId = "62cb5db0193a07c867079bac"
        self._db = MainStorageProvider()

    #

    def getTypes(self) -> Dict:
        rawTypesList = self._db.get(self._typesCollectionId)

        return json_util.loads(rawTypesList)

    #

    def updateTypes(self, data: Dict) -> None:
        jsonData = json_util.loads(data)
        self._validateExpenseTypes(jsonData)

        currentTypes = self.getTypes()
        types = set(jsonData.types)

        newTypes = {"_id": ObjectId(currentTypes["_id"]), "types": types}

        self._db.save(newTypes)

    #

    def _validateTypes(self, data: Dict) -> None:
        if "types" not in data.types:
            raise Exception("invalid types object")
        #

        if type(data.types) != list:
            raise Exception("types must be a list")
        #

        finalDataTypes = set(data.types)

        for _type in finalDataTypes:
            Type(_type["name"], _type["maxSpend"])

        #

    #


#
