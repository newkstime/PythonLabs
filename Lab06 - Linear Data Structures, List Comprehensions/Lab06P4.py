#a)
powersOfTwo = [2**x for x in range(5) if x > 0]
print("Powers of two:", powersOfTwo)

#b)
powersOfThree = [3**x for x in range(5) if x > 0]
print("Powers of three:", powersOfThree)

powersMatrix = [[ x**y for y in range(5) if y > 0] for x in range(2,7)]
print("Matrix:", powersMatrix)
