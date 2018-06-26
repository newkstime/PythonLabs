def main():
    customerInfo = getData()
    for customer in customerInfo:
        accountNumber, customerType, gallonUsage = customer.split()
        gallonUsage = int(gallonUsage)
        cost = calculateCharge(customerType, gallonUsage)
        print("Account number:", accountNumber, "\nTotal cost:", cost, "\n")

def getData():
    input_file = open("water.txt", "r")
    customerInfo = []
    for customer in input_file:
        customer = customer.strip("\n")
        customerInfo.append(customer)
    return customerInfo
    input_file.close()

def calculateCharge(customerType, gallonUsage):
    if customerType == "r":
        rate = 0.005
        overRate = 0.007
        usageCap = 6000
        if gallonUsage <= usageCap and gallonUsage >= 0:
            cost  = gallonUsage * rate
            return cost
        elif gallonUsage > usageCap:
            cost = (usageCap * rate) + ((gallonUsage - usageCap) * overRate)
            return cost
        else:
            print("Invalid usage amount. Exiting")
            quit()
    elif customerType == "b":
        rate = 0.006
        overRate = 0.008
        usageCap = 8000
        if gallonUsage <= usageCap and gallonUsage >= 0:
            cost  = gallonUsage * rate
            return cost
        elif gallonUsage > usageCap:
            cost = (usageCap * rate) + ((gallonUsage - usageCap) * overRate)
            return cost
        else:
            print("Invalid usage amount. Exiting...")
            quit()
    else:
        print("Invalid customer type. Exiting...")
        quit()

main()
