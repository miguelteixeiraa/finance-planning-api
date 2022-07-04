from db.MainStorageProvider import MainStorageProvider
from typing import Dict


class ExpensesService:
    def __init__(self) -> None:
        self._typesId = "62c230fc1473bd80d91cf1f1"
        self._db = MainStorageProvider()

    #

    def getExpenseTypes(self) -> Dict:
        return self._db.get(self._typesId)

    #

    def updateExpenseTypes(self, data: Dict) -> None:
        self._validateExpenseTypes(data)
        self._db.save(data)

    #

    def _validateExpenseTypes(self, data: Dict):
        for _type in data.types.keys():
            if "maxSpend" not in data.types[_type].keys():
                raise Exception("A type must contain a maxSpend field")
            #
        #

    #
