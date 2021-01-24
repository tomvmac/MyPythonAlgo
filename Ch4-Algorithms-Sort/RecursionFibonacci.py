# Fibonacci

# Definition of Fibonacci Series:
# 1. It's a series of integers
# 2. Value of the nth integer can be found by adding the values of the two previous
# integers in the series
# 3. The series starts off with 0, 1, 1, 2, 3, 5, 8, not 13..
# 4. What would be the base case if we were to do this recursively?


# Logic
# fib(2) = 1 + 1 or fib(1) + fib(0)
# fib (3) = 2 + 1 or fib(2) + fib(1)

def fib_recur(n):
    # Base cases
    if n == 0:
        return 0

    if n==1:
        return 1

    # Recursive Body
    return fib_recur(n-1) + fib_recur(n-2)

def fib_runner(z):
    print(f"The {z}th number in the fibonacci sequence is {fib_recur(z)}")


z = 0
fib_runner(z)
z = 1
fib_runner(z)
z = 3
fib_runner(z)
z = 5
fib_runner(z)
z = 6
fib_runner(z)
z = 7
fib_runner(z)
z = 8
fib_runner(z)
z = 9
fib_runner(z)
z = 10
fib_runner(z)