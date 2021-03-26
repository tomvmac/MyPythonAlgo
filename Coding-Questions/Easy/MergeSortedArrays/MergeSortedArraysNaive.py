# Merge Sorted Array

# Given two sorted arrays num1 and nums2, merge num2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively.  You may assume nums1 hhas a size equal to m + n such
# that it has enough space to hold additional elements from nums2.

# General strategy
# 1. Append all nums2 elements to nums1
# 2. Sort nums1

# Time Complexity: O(n), because O(n) for loop, then O(log(n)) for sorting
class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        indexToInsert = 0
        for i in range(n):
            indexToInsert = m + i
            nums1[indexToInsert] = nums2[i]
        nums1.sort()


# Driver Code
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

expectedOutput = [1, 2, 2, 3, 5, 6]


solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)