from Problem1.dinner_combo import Dinner_combo

class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self):
        base = super()
        base.__init__()
        self._appitizer = ''

    def choose_appetizer(self):
        appetizer = input("Please choose your appetizer. For Spring Roll($1.25) enter [1]. For Chicken Wing($1.50) enter [2]: ")
        while appetizer != '1' and appetizer !='2':
            print("Invalid selection. Please try again.")
            appetizer = input("Please choose your appetizer. For Spring Roll($1.25) enter [1]. For Chicken Wing($1.50) enter [2]: ")
        if appetizer == '1':
            self._appetizer = "Spring Roll"
            self._total += 1.25
        elif appetizer == '2':
            self._appetizer = "Chicken Wing"
            self._total += 1.5

    def display_order(self):
        print("Items ordered: ", self._main_dish, ", ", self._soup, ", ", self._appetizer)
        print("Total: ${0:.2f}".format(self._total))
