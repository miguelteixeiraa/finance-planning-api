class Expense:
    def __init__(self, expenseType, cost, description):
        self._type = expenseType
        self._cost = cost
        self._description = description

        self._validateExpense()

    #

    def _validateExpense(self):
        if not self._cost:
            raise Exception("an expense should have a cost")
        #


#
