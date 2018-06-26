class Utility_bill:

    def __init__(self, customer_name, customer_address):
        self._customer_name = customer_name
        self._customer_address = customer_address
        self._total = 0

    def calculate_charge(self):
        raise NotImplementedError("Method calculate_charge has no implementation.")

    def display_bill(self):
        raise NotImplementedError("Method display_bill has no implementation.")
