def main():
    numberOfLabs = int(input("How many labs are you entering?"))
    while numberOfLabs <= 0:
        print("Invalid input")
        numberOfLabs = int(input("How many labs are you entering?"))

    labScores = []
    i = 0
    while i < numberOfLabs:
        score = float(input("Enter a lab score:"))
        labScores.append(score)
        i += 1
    print("Lab scores:", labScores)

    numberOfTests = int(input("How many tests are you entering?"))
    while numberOfTests <= 0:
        print("Invalid input")
        numberOfTests = int(input("How many tests are you entering?"))

    testScores = []
    i = 0
    while i < numberOfTests:
        score = float(input("Enter a test score:"))
        testScores.append(score)
        i += 1
    print("Test scores:", testScores)

    print("The default weight for scores is 50% labs and 50% tests.")
    weightSelection = input("To change weight scale enter C, to use default weights, enter D:").lower()
    while weightSelection != "c" and weightSelection != "d":
        print("Invalid input.")
        weightSelection = input("To change weight scale enter C, to use default weights, enter D:").lower()
    if weightSelection == "c":
        labWeight =  float(input("What % weight do you want labs to count for? (Do not use % sign):"))
        while labWeight < 0:
            print("Invalid input.")
            labWeight =  float(input("What % weight do you want labs to count for? (Do not use % sign):"))
        testWeight = float(input("What % weight do you want tests to count for? (Do not use % sign):"))
        while testWeight < 0:
            print("Invalid input.")
            testWeight = float(input("What % weight do you want tests to count for? (Do not use % sign):"))
        grade_calculator(labScores, testScores, labWeight, testWeight)
    else:
        grade_calculator(labScores, testScores)

def grade_calculator(labScores, testScores, labWeight = 50, testWeight = 50):
    labAverage = sum(labScores) / len(labScores)
    print("Lab Average:", labAverage)

    testAverage = sum(testScores) / len(testScores)
    print("Test Average:", testAverage)

    courseGrade = (labAverage * (labWeight/100)) + (testAverage * (testWeight/100))
    print("Course Grade:", courseGrade)

main()
