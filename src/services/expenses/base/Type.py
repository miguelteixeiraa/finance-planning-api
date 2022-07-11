class Type:
    def __init__(self, name, maxSpend, id):
        self._name = name
        self._maxSpend = maxSpend
        self._validateType()

    #

    def _validateType(self) -> None:
        if type(self._name) != str or not self._name.strip():
            raise Exception("")

        if self._maxSpend < 0:
            raise Exception()
        #

    #

    def getName(self) -> str:
        return self._name

    #

    def getMaxSpend(self) -> float:
        return self._maxSpend

    #


#
