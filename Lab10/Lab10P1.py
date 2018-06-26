def main():
    clearFile()
    times = 0
    while times < 4:
        accountNumber, customerType, gallonsUsed = getInput()
        writeOutput(accountNumber, customerType, gallonsUsed)
        times += 1

def getAccountNumber():
    accountNumber = input("Enter your account number:")
    while accountNumber.isdigit() == False:
        print("Invalid account number. Please try again.")
        accountNumber = input("Enter your account number:")
    return accountNumber

def getCustomerType():
    customerType = input("Enter your customer type. R for residential, B for business:")
    customerType = customerType.lower()
    while customerType != "r" and customerType !="b":
        print("Invalid customer type:")
        customerType = input("Enter your customer type. R for residential, B for business:")
        customerType = customerType.lower()
    return customerType

def getGallonsUsed():
    gallonsUsed = input("Enter the number of gallons of water used:")
    while gallonsUsed.isdigit() == False:
        print("Invalid amount. Please try again.")
        gallonsUsed = input("Enter the number of gallons of water used:")
    testNumber = float(gallonsUsed)
    while testNumber < 0:
        print("Invalid amount. Please try again.")
        gallonsUsed = input("Enter the number of gallons of water used:")
    return gallonsUsed

def getInput(customerType = "", accountNumber = "", gallonsUsed = ""):
    accountNumber = getAccountNumber()
    customerType = getCustomerType()
    gallonsUsed = getGallonsUsed()
    return accountNumber, customerType, gallonsUsed

def writeOutput(accountNumber, customerType, gallonsUsed):
    output_file = open("water.txt", "a")
    output_file.write(accountNumber)
    output_file.write(' ')
    output_file.write(customerType)
    output_file.write(' ')
    output_file.write(gallonsUsed)
    output_file.write(' \n')
    output_file.close()

def clearFile():
    output_file = open("water.txt", "w")
    output_file.write("")

main()
