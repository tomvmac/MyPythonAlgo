# First Duplicate Value

# Give an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that
# returns the first integer that appears more than once (when the array is read from left to right)

# In other words, out of all the integers that might occur more than once in the input array, your function should
# return the one whose first duplicate value has the minimum index.

# If no integer appears more than once, your function should return -1.

# Note that you're allowed to mutate the input array.

# General Strategy
# 1. Iterate through array
# 2. Put item in array if not exist, if exist, return index, first duplicate found

# Time: O(n)
# Space: O(n)

def firstDuplicateValue(array):
    foundItems = {}

    # Iterate through array
    for index in range(len(array)):
        if array[index] in foundItems:
            return array[index]
        else:
            foundItems[array[index]] = 1

    return -1




# Driver Code
array = [2, 1, 5, 2, 3, 3, 4]

print(firstDuplicateValue(array))