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
# 1. Loop starting from the end of the string, one char at a time.
# 2. Use two pointers head and tail, both initially assigned to the end of the array.
# 3. Decrement head until space is found
# 4. Append chars from head to tail to return string
# 5. Move tail to head
# 6. Continue decrementing until head is not space
# 7. Append chars from head to tail


def reverseWordsInString(string):
    charArray = list(string)
    reversedWordsArray = []
    tail = len(charArray)-1
    head = tail
    isProcessingWhitespace = False

    while head > 0:
        if charArray[head] == ' ':
            isProcessingWhitespace = True
        else:
            isProcessingWhitespace = False

        if isProcessingWhitespace:
            # Process Whitespace
            # Move until character is no longer whitespace
            while charArray[head] == ' ' and head > 0:
                head -= 1
        else:
            # Process word
            while charArray[head] != ' ' and head > 0:
                head -= 1

        # Gather word or whitespaces and append to return array
        if head > 0:
            start = head + 1
        else:
            start = head

        for i in range(start, tail+1):
            reversedWordsArray.append(charArray[i])
        tail = head

    return "".join(reversedWordsArray)


# Driver Code
string = "AlgoExpert is the best!"
string = "1 12 23 34 56"
string = "a dog is a man's best f"
print(reverseWordsInString(string))

