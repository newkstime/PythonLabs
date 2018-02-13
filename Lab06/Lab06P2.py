#Tuple of 10 random numbers from 1 to 15
from random import randint
intList = [randint(0,15) for p in range(0,10)]
intTuple = tuple(intList[:])
print("Tuple of 10 random numbers:", intTuple)

#Tuple of the first 3 numbers
firstThreeTuple = intTuple[:3]
print("Tuple of the first 3 numbers:", firstThreeTuple)
#Tuple of the last 3 numbers
lastThreeTuple = intTuple[-3:]
print("Tuple of the last 3 numbers:", lastThreeTuple)
#Concat the last two tuples
concatTuple = tuple(firstThreeTuple + lastThreeTuple)
print("Tuple of the concatenated tuples:", concatTuple)
sortedConcatList = []
for x in firstThreeTuple:
    sortedConcatList.append(x)
for x in lastThreeTuple:
    sortedConcatList.append(x)
sortedConcatList.sort()
sortedConcatTuple = tuple(sortedConcatList)
print("Tuple of the sorted concatenated tuples:", sortedConcatTuple)
