jackpot = int(input("Enter in the jackpot amount:"))
jackpot_annual = jackpot / 20
jackpot_annual_taxed = jackpot_annual * .70
jackpot_lump = jackpot * .65
jackpot_lump_taxed = jackpot_lump * .70
print("Your pre tax annual installment amount is: $", format(jackpot_annual, ",.2f"))
print("Your annual installment amount after tax is: $", format(jackpot_annual_taxed, ",.2f"))
print("Your pre tax lump sum amount is: $", format(jackpot_lump, ",.2f"))
print("Your lump sum amount after tax is: $", format(jackpot_lump_taxed, ",.2f"))
