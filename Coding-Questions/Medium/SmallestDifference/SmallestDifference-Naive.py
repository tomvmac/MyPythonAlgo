# Smallest Difference
# Write a function that takes in two non-empty array of integers, finds the pair of numbers (one from each array) whose
# absolute difference is closest to zero, and returns an array containing these two numbers, with the number from the first
# array in the first position.

# Note that the absolute difference of two integers is the distance between them on the real number line.  For example, the
# absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

# You can assume that there will only be one pair of numbers with the smallest difference.


# General strategy
# 1. loop through array1 and then array2
# 2. calc abs currDiff as abs(array1[i] - array2[j])
# 3. compare currDiff to smallest diff, if smallest diff is None, then assign
#    a. if currDiff


def smallestDifference(arrayOne, arrayTwo):
    smallestDiff = None
    smallestDiffArray = []
    currDiff = 0

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            currDiff = abs(arrayOne[i] - arrayTwo[j])
            if smallestDiff is None:
                smallestDiff = currDiff
            elif currDiff < smallestDiff:
                smallestDiff = currDiff
                if smallestDiffArray != []:
                    smallestDiffArray.pop()
                    smallestDiffArray.pop()
                smallestDiffArray.append(arrayOne[i])
                smallestDiffArray.append(arrayTwo[j])
    return smallestDiffArray




# Driver code

arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

expectedArray = [28, 26]

print("expectedArray", expectedArray)
print("actualArray", smallestDifference(arrayOne, arrayTwo))