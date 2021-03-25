# Min Number of Coins For Change

# Given an array of positive integers representing coin demoninations and a single non-negative integer n representing a target amount of money,

# Write a function that returns the smallest number of coins needed to make change for (to sum up to) that target amount using the given coin
# denominations.

# Note that you have access to an unlimited amount of coins.  In other words, if the denominations are [1, 5, 10], you have access to an unlimited
# amount of 1s, 5s, 10s.

# if its impossible to make change for the target amount, return -1.

# General Strategy
# 1. Sort array of coins
# 2. Loop through from greatest to smallest
#    a. Divide target by  coinValue, store number of times divided
#    b. Modulus to get remainder, if there is remainder continue


def minNumberOfCoinsForChange(n, denoms):
    numOfCoinsToReturn = 0
    remainder = n
    idx = len(denoms)-1

    # sort array
    denoms.sort()

    while remainder > 0 and idx >= 0:
        if remainder > 0:
            n = remainder

        coinsDivided = n // denoms[idx]
        remainder = n % denoms[idx]

        if coinsDivided > 0:
            numOfCoinsToReturn += coinsDivided

        idx -= 1


    if remainder > 0:
        return -1
    else:
        return numOfCoinsToReturn





# Driver Code
# n = 7
# denoms = [1, 5, 10]

# n = 10
# denoms = [1, 5, 10]

n = 9
denoms = [3, 5]

print(minNumberOfCoinsForChange(n, denoms))
