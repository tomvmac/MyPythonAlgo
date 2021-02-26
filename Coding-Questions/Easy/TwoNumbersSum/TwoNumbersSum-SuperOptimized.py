# Two Number Sum:
#
# Write a function that takes in a non-empty array of distinct integers and an integer representing
# a target sum. If any two numbers in the input array sum up to the target sum,
# the function should return them in an array, in any order.
#
# If no two numbers sum up to the target sum, the function should return an empty array.
#
#
# Sample Input:
#
# array = [3, 5, -4, 8, 11, 1, -1, 6]
# targetSum = 10

# Time Complexity: o(n log (n))
# Space Complexity: o(1)

def twoNumberSum(arr1, targetSum):
    sumArr = []

    # General Solution
    # Sort the array first
    # Iterate through 1 loop
    # Include two pointers a left and a right pointer
    # Add left and right pointer values and compare to targetSum, if less than targetSum move left point to the right
    #   otherwise, move right pointer to the left
    # do this until combo found or no more moves

    # 1. init a hash table
    # 2. potentialMatch = targetSum - arr1[num1]
    # 3. if potentialMatch in hash table, return potentialMatch and arr1[num1]
    # 4. else add arr1[num1] to hash table


    # sort the array
    arr1.sort()

    # init left and right pointers
    left = 0
    right = len(arr1) - 1

    while left < right:
        currentSum = arr1[left] + arr1[right]
        if currentSum == targetSum:
            sumArr.append(arr1[left])
            sumArr.append(arr1[right])
            return sumArr
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return sumArr




arr1 = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

sumArr = twoNumberSum(arr1, targetSum)

print(sumArr)


