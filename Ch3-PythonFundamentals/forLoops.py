# Loops

from random import randint, choice
from string import ascii_lowercase

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
my_dict = {'py': 'python', 'rb': 'ruby', 'js': 'javascript'}

# sum of all ints
sum = 0
for num in l:
    sum = sum + num

print(f"Sum using list: {sum}")

# range generator
sum = 0
for num in range(10):
    print(num)
    print("hello")
    print(l[num])

sum = 0
for num in range(len(l)):
    sum += l[num]
print(f"Sum using range generator: {sum}")

# starting range at another number, include step size as well


# iterate through items in dict
for item in my_dict.items():
    print(item)
    # unpack key value pairs into tuple
    key, value = item
    print(f"key = {key}, value = {value}")

# another way to unpack key values is to do it on the for loop
for key, value in my_dict.items():
    # unpack key value pairs into tuple
    print(f"key = {key}, value = {value}")

# list comprendhension - list generator of random numbers

# generate 100 random integers between 1 and 100
l1 = []
for num in range(100):
    l1.append(randint(1, 100))
print(l1)

# generate using list comprehension
l2 = [randint(1, 100) for num in range(100)]
print(l2)

# random strings
l3 = [choice(ascii_lowercase) for num in range(1, 100)]
print(l3)