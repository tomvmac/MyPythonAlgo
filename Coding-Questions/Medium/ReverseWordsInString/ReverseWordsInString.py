# Reverse Words In String

# Write a function that takes in a string of words separated by one or more whitespaces and returns a string that has these words in reverse order.
# "tim is great", your function should return "great is tim"

# For this problem, a word can contain special characters, punctuation and numbers.  The words in the string will be separated by one or more
# whitespaces, and the reversed string must contain the same whitespaces as the original string.

# For example, give the string "whitespaces 4" you should be expected to return "4 whitespaces".

# Note that you're not allowed to use any built-in split or reverse methods/functions.  However, you are allowed to use a built-in join
# method/function.

# Also note that the input string isn't guaranteed to always contain words.

# General Strategy:
# 1. Loop through string get all the words and add to words array
#    a. For each word, startOfWord is reset and checked if it is a whitespace
# 2. Loop through the words array and reverse and return string of it


def reverseWordsInString(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]

        if character == " ":
            # Once we reach a whitespace, append from startOfWord to idx, excluding it
            words.append(string[startOfWord: idx])
            # reset startOfWord
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx


    words.append(string[startOfWord:])

    reverseList(words)

    return "".join(words)

def reverseList(list):
    start, end = 0, len(list) - 1

    while start < end:
        list[start], list[end] = list[end], list[start]
        start += 1
        end -= 1


# Driver Code
string = "AlgoExpert is the best!"
string = "1 12 23 34 56"
string = "a dog is a man's best f"
print(reverseWordsInString(string))

