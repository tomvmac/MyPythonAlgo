# First Duplicate Value

# Give an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that
# returns the first integer that appears more than once (when the array is read from left to right)

# In other words, out of all the integers that might occur more than once in the input array, your function should
# return the one whose first duplicate value has the minimum index.

# If no integer appears more than once, your function should return -1.

# Note that you're allowed to mutate the input array.

# General Strategy
# 1. Iterate through array
# 2. Mark the item with a negative sign, as you go, signifying seen status

# Time: O(n)
# Space: O(1)

def firstDuplicateValue(array):

    # Iterate through array
    for index in range(len(array)):
        absIndex = abs(array[index])
        if array[absIndex - 1] < 0:
            # found the negative index value
            return absIndex
        else:
            # mark item with negative index value
            array[absIndex - 1] *= -1

    return -1




# Driver Code
array = [2, 1, 5, 2, 3, 3, 4]

print(firstDuplicateValue(array))