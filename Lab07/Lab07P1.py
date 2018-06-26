def main():
    kWhUsed = float(input(("Enter kilowatt hours used:")))
    while kWhUsed < 0:
        print("Invalid input.")
        kWhUsed = float(input(("Enter kilowatt hours used:")))
    bill_calculator(kWhUsed)

def bill_calculator(kWhUsed):
    lowRate = 0.12
    highRate = 0.15
    kWhLimit = 500
    if kWhUsed <= kWhLimit:
        charge = kWhUsed * lowRate
    else:
        charge = ((kWhUsed - kWhLimit) * highRate) + (kWhLimit * lowRate)
    print("Please pay this amount:", format(charge, ",.2f"))

main()
