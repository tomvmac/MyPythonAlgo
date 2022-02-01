def reverseString(string):
    reversedList = []

    # conver string to list
    charList = list(string)

    for i in range(len(charList)-1, -1, -1):
        reversedList.append(charList[i])

    return "".join(reversedList)



string1 = "abcd"
print(reverseString(string1))
