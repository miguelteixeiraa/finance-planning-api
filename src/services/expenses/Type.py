class Type:
    def __init__(self, name, maxExpend, id):
        self._name = name
        self._maxExpend = maxExpend

    #

    def validateType(self) -> None:
        if type(self._name) != str or not self._name.strip():
            raise Exception("")

        if self._maxExpend < 0:
            raise Exception()
        #

    #

    def getName(self) -> str:
        return self._name

    #

    def getMaxExpend(self) -> float:
        return self._maxExpend

    #
#
