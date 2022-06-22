import functools
import operator
import json
from typing import Number


class ExpenseType:
    def __init__(self, label: str, maxSpend: Number) -> None:
        if label == "" or maxSpend < 0:
            raise Exception("Failed to create ExpenseType")
        self.__label = label
        self.__maxSpend = maxSpend
        self.__entries = []

    #

    def appendEntry(self, expenseEntry) -> None:
        self.__entries.append(expenseEntry)

    #

    def getCurrentSpend(self) -> Number:
        return functools.reduce(operator.add, self.__entries)

    #

    def toJson(self) -> str:
        return json.dumps(
            {
                "name": self.__label,
                "entries": self.__entries,
                "maxSpend": self.__maxSpend,
            }
        )


#
