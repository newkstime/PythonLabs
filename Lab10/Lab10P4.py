word = input("Enter a string:")
word = word.upper()
filterWord = ''.join(filter(lambda x: x.isalpha(), word))
print(filterWord)

while len(filterWord) > 0:
    count = filterWord.count(filterWord[0])
    print (filterWord[0], " ", count)
    filterWord = filterWord.replace(filterWord[0], "")
