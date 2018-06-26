class Dinner_combo:

    def __init__(self):
        self._main_dish = ''
        self._soup = ''
        self._total = 0

    def choose_main_dish(self):
        main_dish = input("Please choose your main dish. For Sweet & Sour Pork ($7) enter [1]. For Sesame Chicken ($8) enter [2]. For Shrimp Fried Rice($9) enter [3]: ")
        while main_dish != '1' and main_dish !='2' and main_dish !='3':
            print("Invalid selection. Please try again.")
            main_dish = input("Please choose your main dish. For Sweet & Sour Pork ($7) enter [1]. For Sesame Chicken ($8) enter [2]. For Shrimp Fried Rice($9) enter [3]: ")
        if main_dish == '1':
            self._main_dish = "Sweet and Sour Pork"
            self._total += 7
        elif main_dish == '2':
            self._main_dish = "Sesame Chicken"
            self._total += 8
        elif main_dish == '3':
            self._main_dish = "Shrimp Fried Rice"
            self._total = 9

    def choose_soup(self):
        soup = input("Please choose your soup. For Egg Drop Soup ($1.25) enter [1]. For Wonton Soup ($1.50) enter [2]: ")
        while soup != '1' and soup != '2':
            print("Invalid selection. Please try again.")
            soup = input("Please choose your soup. For Egg Drop Soup ($1.25) enter [1]. For Wonton Soup ($1.50) enter [2]: ")
        if soup == '1':
            self._soup = "Egg Drop Soup"
            self._total += 1.25
        elif soup == '2':
            self._soup = "Wonton Soup"
            self._total += 1.5

    def display_order(self):
        print("Items ordered: ", self._main_dish, ", ", self._soup)
        print("Total: ${0:.2f}".format(self._total))
