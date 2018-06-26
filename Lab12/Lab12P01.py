def main():
    count, total = scanPrices()
    total = discount(count, total)
    count, total = promotion(count, total)
    makePayment(total)

def scanPrices():
    numberOfItems = 0
    total = 0
    while True:
        try:
            itemPrice = float(input("Enter the price of the item [To exit, enter 0]:"))
            while itemPrice < 0:
                print("Price cannot be negative.")
                itemPrice = float(input("Enter the price of the item [To exit, enter 0]:"))
            if itemPrice == 0:
                return numberOfItems, total
            numberOfItems += 1
            total += itemPrice
            print("Number of items purchase:", numberOfItems)
            print("Total cost of items: $", format(total, ".2f"))
        except ValueError:
            print("Price must be entered with numbers and decimals only.")

def discount(count, total):
    itemsNeededForDiscount = 10
    discountRate = .10
    if count >= itemsNeededForDiscount:
        total = total - (total * discountRate)
        print("You received a", discountRate * 100,"% discount for purchasing", itemsNeededForDiscount, "or more items.")
        print("Your new total is: $", format(total, ".2f"))
    return total

def promotion(count, total):
    totalNeededForPromotion = 50
    if total >= totalNeededForPromotion:
        purchaseGiftCard = input("Would you like to purchase a $50 gift card for $40?[Y/N]")
        while purchaseGiftCard != "Y" and purchaseGiftCard != "N" and purchaseGiftCard != "y" and purchaseGiftCard != "n":
            print("Invalid input. Please try again.")
            purchaseGiftCard = input("Would you like to purchase a $50 gift card for $40?[Y/N]")
        if purchaseGiftCard == "Y" or purchaseGiftCard == "y":
            print("You have purchased a gift card.")
            total += 40
            count += 1
            print("Number of items purchase:", count)
            print("Total cost of items: $", format(total, ".2f"))
    return count, total

def makePayment(balance):
    paymentType = input("Please enter [1] to pay with cash or [2] to pay with debit:")
    while paymentType != "1" and paymentType != "2":
        print("Invalid entry.")
        paymentType = input("Please enter [1] to pay with cash or [2] to pay with debit:")
    if paymentType == "1":
        payCash(balance)
    elif paymentType == "2":
        payDebit(balance)

def payCash(balance):
    paymentTotal = 0
    while float(paymentTotal) < float(balance):
        print("This machine only accepts cash payment int he form of $10, $5, and $1 bills.")
        numberOfTens = input("Please enter then number of $10 bills:")
        while numberOfTens.isdigit() != True or int(numberOfTens) < 0:
            print("Invalid entry")
            numberOfTens = input("Please enter then number of $10 bills:")
        numberOfFives = input("Please enter then number of $5 bills:")
        while numberOfFives.isdigit() != True or int(numberOfFives) < 0:
            print("Invalid entry")
            numberOfFives = input("Please enter then number of $5 bills:")
        numberOfOnes = input("Please enter then number of $1 bills:")
        while numberOfOnes.isdigit() != True or int(numberOfOnes) < 0:
            print("Invalid entry")
            numberOfOnes = input("Please enter then number of $1 bills:")
        paymentTotal = (int(numberOfTens) * 10) + (int(numberOfFives) * 5) + (int(numberOfOnes))
        if int(paymentTotal) < int(balance):
            print("Error: Total payment is less than owed balance. Please reenter:")
    print("Thank you for your payment.")
    changeReturned = float(paymentTotal) - (float(balance))
    print("Change returned:$", format(changeReturned, ".2f"))

def payDebit(balance):
    cardNumber = input("Please enter your 16-digit card number:")
    while cardNumber.isdigit() != True or len(cardNumber) != 16:
        print("Invalid card number.")
        cardNumber = input("Please enter your 16-digit card number:")
    cardPin = input("Please enter your 4 digit card pin:")
    while cardNumber.isdigit() != True or len(cardPin) != 4:
        print("Invalid pin number.")
        cardPin = input("Please enter your 4 digit card pin:")
    paymentTotal = input("Please enter your payment amount:")
    isPaymentValid = False
    while isPaymentValid == False:
        if paymentTotal.isdigit() != True:
            print("Invalid entry.")
            paymentTotal = input("Please enter your payment amount:")
        elif float(paymentTotal) < float(balance):
            print("Error: Total payment is less than owed balance. Please reenter.")
            paymentTotal = input("Please enter your payment amount:")
        else:
            isPaymentValid = True
    print("Thank you for your payment.")

main()
