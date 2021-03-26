# Merge Sorted Array

# Given two sorted arrays num1 and nums2, merge num2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively.  You may assume nums1 hhas a size equal to m + n such
# that it has enough space to hold additional elements from nums2.


class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1




# Driver Code
nums1 = [1,2,3,0,0,0]
m = 3
# nums2 = [2,5,6]
nums2 = [1,1,2]
n = 3

expectedOutput = [1, 2, 2, 3, 5, 6]


solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)