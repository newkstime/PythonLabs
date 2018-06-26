valid_hotdogs = False
while valid_hotdogs == False:
    try:
        hotdogs = int(input("How many hotdogs are purchased?:"))
        valid_hotdogs = True
    except ValueError:
        print("Invalid input.")

valid_potato_chips = False
while valid_potato_chips == False:
    try:
        potato_chips = int(input("How many potato chips are purchased?:"))
        valid_potato_chips = True
    except ValueError:
        print("Invalid input.")

valid_sodas = False
while valid_sodas == False:
    try:
        sodas = int(input("How many sodas are purchased?:"))
        valid_sodas = True
    except ValueError:
        print("Invalid input.")

hotdogs_total = hotdogs * 2.50
potato_chips_total = potato_chips * 1.50
sodas_total = sodas * 1.25
grand_total = format(hotdogs_total + potato_chips_total + sodas_total, '.2f')
print("Your total is $",grand_total)
