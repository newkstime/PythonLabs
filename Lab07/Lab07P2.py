def main():
    kWhUsed = float(input(("Enter kilowatt hours used:")))
    while kWhUsed < 0:
        print("Invalid input.")
        kWhUsed = float(input(("Enter kilowatt hours used:")))
    customerType= input("Are you a Residential[R] or Business[B] customer? [R/B]:").lower()
    while customerType != "r" and customerType != "b":
        print("Invalid input.")
        customerType = input("Are you a Residential[R] or Business[B] customer? [R/B]").lower()
    bill_calculator(kWhUsed, customerType)

def bill_calculator(kWhUsed, customerType):
    if customerType == "r":
        lowRate = 0.12
        highRate = 0.15
        kWhLimit = 500
        if kWhUsed <= kWhLimit:
            charge = kWhUsed * lowRate
        else:
            charge = ((kWhUsed - kWhLimit) * highRate) + (kWhLimit * lowRate)
    elif customerType == "b":
        lowRate = 0.16
        highRate = 0.20
        kWhLimit = 800
        if kWhUsed <= kWhLimit:
            charge = kWhUsed * lowRate
        else:
            charge = ((kWhUsed - kWhLimit) * highRate) + (kWhLimit * lowRate)
    print("Please pay this amount: $", format(charge, ",.2f"))

main()
