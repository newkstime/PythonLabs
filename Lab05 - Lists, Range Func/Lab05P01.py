listOfInt = []
acceptableRange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Prompt user for integers between 1 and 10 until they enter "n"
addInt = "y"
while addInt == "y":
    intToAdd = int(input("Please enter an integer from 1 to 10:"))
    while intToAdd not in acceptableRange:
        print("ERROR: Integer is invalid.")
        intToAdd = int(input("Please enter an integer from 1 to 10:"))
    listOfInt.append(intToAdd)
    addInt = input("Would you like to enter another integer [y/n]?")
    while addInt.lower() != "y" and addInt.lower() != "n":
        print("ERROR: Incorrect input.")
        addInt = input("Would you like to enter another integer [y/n]?")
#Display list
print(listOfInt)
#Display the average of the list
i = 0
total = 0
while i < len(listOfInt):
    total += listOfInt[i]
    i += 1
listAverage = total / len(listOfInt)
print(listAverage)
#If the average is > 7, subtract 1 from each number in the list.
modifiedList = []
if listAverage > 7:
    j = 0
    while j < len(listOfInt):
        modifiedInt = (listOfInt[j] - 1)
        modifiedList.append(modifiedInt)
        j += 1
    #Display the modified list
    print(modifiedList)
