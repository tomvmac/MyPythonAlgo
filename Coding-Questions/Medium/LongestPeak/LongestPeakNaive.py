# Longest Peak

# Write a function that takes an array on integers and returns the length of the longest peak in the array.

# A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip
# (the highest value in the peak), at which point they become strictly decreasing.
# At least three integers are required to form a peak.

# For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.

# Similarly, the integers 1, 2, 3 don't form a peak because they are strictly decreasing after the 3.

# General strategy
# 1. Loop (outer loop)
# 2. Inner Loop (while loop)
# 3. Compare curr and next to see if forms a peak (strictly increasing or strictly decreasing, if so store the longestPeak
#     a. next peak, compare to longestPeak, if >, swap


def longestPeak(array):
    longestPeak = 0

    for num in range(len(array)):
        strictlyAscending = True
        strictlyDescending = True
        peakCount = 0

        left = num
        right = num + 1
        while right < len(array):
            if array[left] < array[right]:
                strictlyAscending = True
                peakCount += 1
            elif array[right] > array[right]:
                strictlyDescending = True
                peakCount += 1
            else:
                strictlyAscending = False
                strictlyDescending = False

            left += 1
            right += 1

        if peakCount > 2 and peakCount > longestPeak:
            longestPeak = peakCount

    return longestPeak


# Driver Code

# array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
array = [1, 3, 2]
print(longestPeak(array))