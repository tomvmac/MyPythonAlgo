# Find Three Largest Numbers

# Write a function that takes in an array of at least three integers and, without sorting the input
# array, returns a sorted array of the three largest integers in the input array.

# function should return duplicate integers if necessary:

# Time: O(n)
# Space: O(1)

# Overall Strategy
# 1. Create an threeNums array with three empty elements
# 2. Iterate through array and compare each item to each of the items on the threeNums array starting from the right, assuming that is the largest
# 3. If array item > threeNums item:
#     a. shift existing values to the left
#     b. insert array item into value


def shiftLeft(array, index, numToAdd):

    if index > 1:
        array[index-2] = array[index-1]
    if index > 0:
        array[index-1] = array[index]
    array[index] = numToAdd

    return array


def findThreeLargestNumbers(array):
    threeLargestNums = [None, None, None]
    itemInserted = False

    # iterate through array
    for i in range(len(array)):
        # insert into appropriate slot in threeLargestNums and shift
        # process last position
        itemInserted = False

        # process last position
        if itemInserted == False:
            if threeLargestNums[2] == None or array[i] >= threeLargestNums[2]:
                if threeLargestNums[2] == None:
                    threeLargestNums[2] = array[i]
                else:
                    if array[i] >= threeLargestNums[2]:
                        threeLargestNums = shiftLeft(threeLargestNums, 2, array[i])
                itemInserted = True

        # process middle position
        if itemInserted == False:
            if threeLargestNums[1] == None or array[i] >= threeLargestNums[1]:
                if threeLargestNums[1] == None:
                    threeLargestNums[1] = array[i]
                else:
                    if array[i] >= threeLargestNums[1]:
                        threeLargestNums = shiftLeft(threeLargestNums, 1, array[i])
                itemInserted = True

        # process first position
        if itemInserted == False:
            if threeLargestNums[0] == None or array[i] >= threeLargestNums[1]:
                if threeLargestNums[0] == None:
                    threeLargestNums[0] = array[i]
                else:
                    if array[i] >= threeLargestNums[0]:
                        threeLargestNums = shiftLeft(threeLargestNums, 0, array[i])
                itemInserted = True

    return threeLargestNums



# Driver Code
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# array = [10, 5, 9, 10, 12]

print(findThreeLargestNumbers(array))