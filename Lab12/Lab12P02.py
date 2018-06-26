import currency

def main():
    print("US Dollar to Foreign Currency Converter")
    selected_currency = input("Please select a currency to convert to. [1] For Euro €. [2] For Japanese Yen ¥. [3] For Mexican Peso $:")
    while selected_currency != "1" and selected_currency != "2" and selected_currency != "3":
        print("Error. Invalid Selection.")
        selected_currency = input("Please select a currency to convert to. [1] For Euro €. [2] For Japanese Yen ¥. [3] For Mexican Peso $:")
    dollar_valid_entry = False
    while dollar_valid_entry == False:
        dollar = input("Please enter the amount of US Dollars to convert:")
        try:
            dollar = float(dollar)
            dollar_valid_entry = True
            while dollar < 0:
                print("US Dollar value cannot be negative.")
                dollar_valid_entry = False
                break
        except ValueError:
            print("Invalid entry.")
    if selected_currency == "1":
        euro = currency.to_euro(dollar)
        print("$" + format(dollar, ".2f"), "is converted to", format(euro, ".2f") + "€")
    elif selected_currency == "2":
        yen = currency.to_euro(dollar)
        print("$" + format(dollar, ".2f"), "is converted to JP¥" + format(yen, ".2f"))
    elif selected_currency == "3":
        peso = currency.to_euro(dollar)
        print("$" + format(dollar, ".2f"), "is converted to MEX$" + format(peso, ".2f"))

main()

