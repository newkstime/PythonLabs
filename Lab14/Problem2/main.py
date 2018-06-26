from Problem2.water_bill import Water_bill
from Problem2.electricity_bill import Electricity_bill

def main():
    customer_name = input("Please the name on the account: ")
    customer_address = input("Please enter the address associated with the account: ")
    bill_selection = input("Enter [1] for water bills. Enter [2] for electric bills: ")
    while bill_selection != '1' and bill_selection != '2':
        print("Invalid entry. Please try again.")
        bill_selection = input("Enter [1] for water bills. Enter [2] for electric bills: ")
    if bill_selection == '1':
        selected_bill = Water_bill(customer_name, customer_address)
        selected_bill.calculate_charge()
        selected_bill.display_bill()
    elif bill_selection == '2':
        selected_bill = Electricity_bill(customer_name, customer_address)
        selected_bill.calculate_charge()
        selected_bill.display_bill()

main()
