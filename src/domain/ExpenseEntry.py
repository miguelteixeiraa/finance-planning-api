import json
from typing import Number


class ExpenseEntry:
    def __init__(self, value: Number, description: str) -> None:
        if value < 0 or description == "":
            raise Exception("Invalid value and description for ExpenseEntry")
        self.__value = (value,)
        self.__description = description

    #

    def toJson(self) -> str:
        return json.dumps({"value": self.__value, "description": self.__description})

    #
