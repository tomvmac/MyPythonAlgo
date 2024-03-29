# Nth Fibonacci
# The Fibonacci sequence is defined as follows: the first number is 0, the second is 1,
# and the nth number is the sum of the (n-1)th and (n-2)th numbers.
#
# Write a function that takes in an integer n and returns the nth Fibonacci number.
#
# Important note: the Fibonacci sequence is often defined with its first numbers are F0 = 0 and F1 = 1,
# For the purpose of this question, the first Fibonacci number is F0; therefore,
# getNthFib(1) is equal to F0 and getNthFib(2) is equal to F1, etc.

# Sample input
# n = 2
# Sample output
# 1 // 0, 1

# Sample Input
# n = 6
# Sample Output
# 5 // 0, 1, 1, 2, 3, 5

# Time: O(n)
# Space: O(1)


def getNthFib(n):
    fibArr = [0, 1]

    if n == 0:
        return 0

    if n == 1:
        return 1

    for num in range(2, n):
        fibArr.append(fibArr[num-2] + fibArr[num-1])

    return fibArr[num]



# Driver Code
print("n = 2, should be 1:")
print(getNthFib(2))

print("n = 6, should be 5:")
print(getNthFib(6))
