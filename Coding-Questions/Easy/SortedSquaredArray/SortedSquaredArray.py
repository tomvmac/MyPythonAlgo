# Sorted Squared Array

# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns
# a new array of the same length with the squares of the original integers also sorted in ascending order.

def sortedSquaredArray(array):
    squaredArray = []

    for i in range (len(array)):
        squaredArray.append(array[i] * array[i])
        # sort to handle negative numbers in the array
        squaredArray.sort()

    return squaredArray


# Driver Code
array = [1, 2, 3, 5, 6, 8, 9]

print(sortedSquaredArray(array))