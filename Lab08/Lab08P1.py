def get_kWh_used():
    kWh = float(input("Enter the number of kilowatt hours used:"))
    while kWh < 0:
        print("Invalid input.")
        kWh = float(input("Enter the number of kilowatt hours used:"))
    return kWh

def bill_calculator(kWhUsed):
    lowRate = 0.12
    highRate = 0.15
    kWhLimit = 500
    if kWhUsed <= kWhLimit:
        charge = kWhUsed * lowRate
    else:
        charge = ((kWhUsed - kWhLimit) * highRate) + (kWhLimit * lowRate)
    return charge


def main():
    printBill = bill_calculator(get_kWh_used())
    print("Please pay this amount: $", format(printBill, ",.2f"))

main()
