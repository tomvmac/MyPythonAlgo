# Intersection Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you
# may return the result in any order.

# General strategy
# 1. Sort nums1 and nums2
# 2. Using two pointers, i and j iterate the pointers
#    a. if value of i and j are equal, add to intersectArray and increment both i and j
#    b. if value of i is smaller than value of j, increment i, otherwise increment j

# Time: O(n)


class Solution:
    def intersect(self, nums1, nums2):
        intersectArray = []
        nums1.sort()
        nums2.sort()

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersectArray.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1


        return intersectArray

# Driver Code
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
# expected = [4, 9]

# nums1 = [1,2,2,1]
# nums2 = [2]
# expected = [2]

solution = Solution()

print(solution.intersect(nums1, nums2))



