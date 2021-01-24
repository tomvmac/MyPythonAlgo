# Factorials

# First Pass look:
# 1! = 1 x 1
# 2! = 2 x 1
# 3! = 3 x 2 x 1
# 4! = 4 x 3 x 2 x 1
# 5! = 5 x 4 x 3 x 2 x 1
#
#
# Second pass look:
# 1! = 1
# 2! = 2 x 1!
# 3! = 3 x 2!
# 4! = 4 x 3!
# 5! = 5 x 4!


def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)

z = 0 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")

z = 1 # expecting 1
print(f"The value of {z}! is {factorial_recur(z)}")

z = 5 # expecting 120
print(f"The value of {z}! is {factorial_recur(z)}")