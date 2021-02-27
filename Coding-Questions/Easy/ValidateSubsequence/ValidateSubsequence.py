# Validate Subsequence
#
# Given two non-empty arrays of integers, write a function that determines whether the second array is
# a subsequence of the first one.
#
#

# A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order
# as they appear in the array. For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4],
# and so do the numbers [2, 4].
#
# Note that a single number in an array and the array itself are both valid subsequences of the array.
#
# Sample Input:
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
#
# Sample Output:
# true

# Solution:
# 1. Iterate through main and child array with while loop
# 2. If main current == sequence current value, set isValidSub = true

# O(n) time
# O(1) space
def isValidSubsequence(arr1, sequence):
    arr1Index = 0
    seqIndex = 0

    while arr1Index < len(arr1) and seqIndex < len(sequence):
        if arr1[arr1Index] == sequence[seqIndex]:
            seqIndex += 1

        arr1Index += 1

    return seqIndex == len(sequence)


# Driver Code

arr1 = [5, 1, 22, 25, 6, -1, 8, 10]
seq1 = [1, 6, -1, 10]

print(isValidSubsequence(arr1, seq1))

arr2 = [5, 1, 22, 25, 6, -1, 8, 10]
seq2 = [5, 1, 22, 25, 6, -1, 8, 10, 12]

print(isValidSubsequence(arr2, seq2))
