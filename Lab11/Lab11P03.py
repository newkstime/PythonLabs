try:
    hotdogs = int(input("How many hotdogs are purchased?:"))
except ValueError:
    print("Amount must be an integer. Setting amount to 0.")
    hotdogs = 0

try:
    potato_chips = int(input("How many potato chips are purchased?:"))
except ValueError:
    print("Amount must be an integer. Setting amount to 0.")
    potato_chips = 0

try:
    sodas = int(input("How many sodas are purchased?:"))
except ValueError:
    print("Amount must be an integer. Setting amount to 0.")
    sodas = 0

hotdogs_total = hotdogs * 2.50
potato_chips_total = potato_chips * 1.50
sodas_total = sodas * 1.25
grand_total = format(hotdogs_total + potato_chips_total + sodas_total, '.2f')
print("Your total is $",grand_total)
