hotdogs = int(input("How many hotdogs are purchased?:"))
potato_chips = int(input("How many potato chips are purchased?:"))
sodas = int(input("How many sodas are purchased?:"))
hotdogs_total = hotdogs * 2.50
potato_chips_total = potato_chips * 1.50
sodas_total = sodas * 1.25
grand_total = format(hotdogs_total + potato_chips_total + sodas_total, '.2f')
print("Your total is $",grand_total)
