# Binary Search

# Write a function that takes in a sorted array of integers as well as a target integer. The function should
# use the Binary Search algorithm to determine if the target integer is contained in the array and should
# return its index if it is, otherwise -1

# General Strategy:
# Determine a start and stop
# Loop using while start < stop
# Find mid point, if equal to target return


# Time - O(n)
# Space

def binarySearch(array, target):
    start = 0
    stop = len(array)-1

    while start <= stop:
        # Find mid
        mid = (start + stop) // 2
        if target == array[mid]:
            # target found
            return mid
        if target > array[mid]:
            # start the right of mid
            start = mid + 1
        else:
            # stop right before mid
            stop = mid - 1

    return -1


# Driver Code

array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

# array = [1, 5, 23, 111]
# target = 5


print(binarySearch(array, target))