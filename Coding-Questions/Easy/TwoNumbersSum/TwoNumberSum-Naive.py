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

# Time Complexity: o(n^2)
# Space Complexity: o(1)

def twoNumberSum(arr1, targetSum):
    sumArr = []

    # General Solution
    # Iterate through 2 loops

    # 1. if indices are diff add values from two arrays
    # 2. if sum equals targetSum, add to sumArr and return


    # Iterate

    for num1 in range(len(arr1)):
        for num2 in range(len(arr1)):
            if num1 != num2:
                if arr1[num1] + arr1[num2] == targetSum:
                    sumArr.append(arr1[num1])
                    sumArr.append(arr1[num2])
                    return sumArr
    return sumArr


arr1 = [3, 5, -4, 8, 11, 1, -1, 6]
arr1 = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

sumArr = twoNumberSum(arr1, targetSum)

print(sumArr)


