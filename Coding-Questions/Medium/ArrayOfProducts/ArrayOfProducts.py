# Array of Products

# Write a function that takes in a non-empty array of integers and returns an array of the same length, where each element in the
# output array is equal to the product of every other number in that input array.

# In other words, the value at output[i] is equal to the product of every number in the input array than input[i]

# Note that you're expected to solve this problem without using division.

# General Strategy:
# Two loops
# 1. loop through
#   a. 2nd loop
#   b. multiple each item in second loop, skipping current item from first loop
#   c. add product to products array

def arrayOfProducts(array):
    productsArray = []

    for i in range(len(array)):
        currProduct = 1
        for j in range(len(array)):
            if j != i:
                currProduct *= array[j]
        productsArray.append(currProduct)

    return productsArray



# Driver Code
array = [5, 1, 4, 2]

# Sample Output
expectedOutput = [8, 40, 10, 20]

print("expectedOutput: ", expectedOutput)
print("actualOutput: ", arrayOfProducts(array))