jeanScore = []
kaylaScore = []
connieScore = []
allScores = [jeanScore, kaylaScore, connieScore]
i = 0
print("Please enter Jean's scores one by one.")
while i < 4:
    score = float(input("Enter a score:"))
    while score < 0:
        print("Invalid score.")
        score = float(input("Enter a score:"))
    jeanScore.append(score)
    i += 1
print("Jean's scores:", jeanScore)
i = 0
print("Please enter Kayla's scores one by one.")
while i < 4:
    score = float(input("Enter a score:"))
    while score < 0:
        print("Invalid score.")
        score = float(input("Enter a score:"))
    kaylaScore.append(score)
    i += 1
print("Kayla's scores:", kaylaScore)
i = 0
print("Please enter Connie's scores one by one.")
while i < 4:
    score = float(input("Enter a score:"))
    while score < 0:
        print("Invalid score.")
        score = float(input("Enter a score:"))
    connieScore.append(score)
    i += 1
print("Connie's scores:", connieScore)

print("All scores:", allScores)

for row in range(3):
    for col in range(4):
        allScores[row][col] += 1
print("All scores after adding a point:", allScores)

for row in range(3):
    allScores[row].sort()
print("All scores after sorting:", allScores)
