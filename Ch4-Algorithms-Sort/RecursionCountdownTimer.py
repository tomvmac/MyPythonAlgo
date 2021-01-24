import time

# RecursionCountdownTimer uses recursion to count down numbers

# recursive function to count down
def recur_countdown_timer(n):
    print(n)
    time.sleep(1)
    if n < 1:
        return
    else:
        return recur_countdown_timer(n-1)



# iterative function to count down
def iter_countdown_timer(n):
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print(n)

z = 5
print(f"Counting down from {z}:")
iter_countdown_timer(z)

recur_countdown_timer(z)