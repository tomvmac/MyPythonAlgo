# Valid IP Addresses

# You're given a stringing of length 12 or smaller, containing only digits.

# Write a function that returns al the possible IP addresses that can be created by inserting three . s in the stringing.

# An IP address is a sequence of four positive integers that are separate by .s, where each individual integer is within the range 0-255, inclusive.

# An IP address isn't valid if any of the individual integers contains leading 0s.  For example, "192.168.0.1" is valid, but 192.168.00.1 and
# 192.168.0.01 are not valid, because they contain 00 and 01 respectively.

# Another example of a valid IP Address is 99.1.1.10 and conversely 991.1.1.0 isn't valid because 991 is greater than 255.

# Your function should return the IP addresses in stringing format and in no particular order.  If no valid IP addresses can be created from the
# stringing, your function should return an empty list.


# General strategy
# Insert periods using all combos

# Time Complexity: O(1) - Constant time, 2 ^32 is the max


def validIPAddresses(string):
    ipAddressesFound = []

    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        # First Period
        currentIPAddressParts[0] = string[:i]
        if not isValidPart(currentIPAddressParts[0]):
            continue

        # Second Period
        for j in range(i + 1, i + min(len(string) - i, 4)):
            currentIPAddressParts[1] = string[i:j]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            for k in range(j + 1, j + min(len(string) - j, 4)):
                currentIPAddressParts[2] = string[j:k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    ipAddressesFound.append(".".join(currentIPAddressParts))

    return ipAddressesFound

def isValidPart(string):
    if len(string) < 1:
        return False

    stringAsInt = int(string)
    if stringAsInt > 255:
        return False

    return len(string) == len(str(stringAsInt)) # check for leading 0s


# Driver Code
string = "1921680"
print(validIPAddresses(string))