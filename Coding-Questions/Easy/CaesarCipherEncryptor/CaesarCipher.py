# Caesar Cipher Encryptor

# Given a non-empty string of lowercase letters and a non-negative integer representing a key,
# write a function that returns a new string obtained by shifting every letter in the input string by k
# positions in the alphabet, where k is the key.

# Note that letters should wrap around the alphabet.  In the other words, the letter z shifted by one
# returns the letter a.

def caesarCipherEncryptor(string, key):
    shiftedArray = []

    # in Python, there are functions for ascii chars
    # ord('a') returns 97
    # chr(97) returns a

    # set charOffset to 96
    wrappedKey = key % 26
    charOffset = 96
    zPosition = 122
    asciiPositionRaw = 0
    asciiPositionAdjusted = 0
    diff = 0

    # split the string into char array
    charArray = list(string)

    # iterate through array
    for char in range(len(charArray)):
        # get ascii code of current char
        currentCharAsciiCode = ord(charArray[char])
        # find the position
        asciiPositionRaw = currentCharAsciiCode + wrappedKey
        if asciiPositionRaw > zPosition:
            # handle the wrap
            diff = asciiPositionRaw - zPosition
            asciiPositionAdjusted = charOffset + diff
        else:
            asciiPositionAdjusted = asciiPositionRaw

        shiftedArray.append(chr(asciiPositionAdjusted))

    return ''.join(shiftedArray)

# Driver Code

string = "xyz"
key = 2

print(string + " with key of " + str(key) + ":")
expectedString = "zab"
print("expected: ", expectedString)

print("actual: ", caesarCipherEncryptor(string, key))


string = "abc"
key = 52

print(string + " with key of " + str(key) + ":")
expectedString = "abc"
print("expected: ", expectedString)

print("actual: ", caesarCipherEncryptor(string, key))