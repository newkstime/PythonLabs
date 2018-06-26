from Problem2.utility_bill import Utility_bill

class Electricity_bill(Utility_bill):

    def __init__(self, customer_name, customer_address):
        base = super()
        base.__init__(customer_name, customer_address)
        self._kwh_used = 0

    def calculate_charge(self):
        while isinstance(self._kwh_used, float) == False or self._kwh_used <= 0:
            try:
                self._kwh_used = float(input("Enter the kWh of electricity used: "))
                while self._kwh_used <= 0:
                    print("Usage cannot be negative.")
                    self._kwh_used = float(input("Enter the kWh of electricity used: "))
            except ValueError:
                print("Invalid entry")
        if self._kwh_used <= 500:
            self._total = self._kwh_used * 0.12
        else:
            self._total = (500 * 0.12) + ((self._kwh_used - 500) * 0.15)

    def display_bill(self):
        print("Electricity Bill\nName: ", self._customer_name, "\nAddress: ", self._customer_address,
              "\nkWh used: ", self._kwh_used, "\nTotal due: ${0:.2f}".format(self._total))
