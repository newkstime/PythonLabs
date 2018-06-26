from Problem2.utility_bill import Utility_bill

class Water_bill(Utility_bill):

    def __init__(self, customer_name, customer_address):
        base = super()
        base.__init__(customer_name, customer_address)
        self._gallons_of_water_used = 0

    def calculate_charge(self):
        while isinstance(self._gallons_of_water_used, float) == False or self._gallons_of_water_used <= 0:
            try:
                self._gallons_of_water_used = float(input("Enter the gallons of water used: "))
                while self._gallons_of_water_used <= 0:
                    print("Gallons used cannot be negative.")
                    self._gallons_of_water_used = float(input("Enter the gallons of water used: "))
            except ValueError:
                print("Invalid entry")
        if self._gallons_of_water_used <= 6000:
            self._total = self._gallons_of_water_used * 0.005
        else:
            self._total = (6000 * 0.005) + ((self._gallons_of_water_used - 6000) * 0.007)

    def display_bill(self):
        print("Water Bill\nName: ", self._customer_name, "\nAddress: ", self._customer_address,
              "\nGallons used: ", self._gallons_of_water_used, "\nTotal due: ${0:.2f}".format(self._total))
