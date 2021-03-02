# Find Three Largest Numbers

# Write a function that takes in an array of at least three integers and, without sorting the input
# array, returns a sorted array of the three largest integers in the input array.

# function should return duplicate integers if necessary:


def findThreeLargestNumbers(array):
    threeLargestNums = []
    temp = 0

    # Insert first three array items into return array
    for i in range(0,3):
        threeLargestNums.append(array[i])

    threeLargestNums.sort()


    # Iterate through the rest of the array
    for i in range(3, len(array)):
        for j in range(0, 3):
            if array[i] > threeLargestNums[j]:
                # replace and break
                threeLargestNums[j] = array[i]
                threeLargestNums.sort()
                break

    return threeLargestNums



# Driver Code
array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

print(findThreeLargestNumbers(array))