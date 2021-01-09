# Tuple example

# Tuples are similar to list, but they are immutable and uses () instead of []

my_random_tuple = ('first', 1, 7, 6, 4, 5, 8, 'hi there', 2, 3, 1, 5, 2, 1, 9, 10)
my_tuple = ('first_value', 'second_value', 'third_value')

# get item from tuple
print(my_tuple[1])
print(my_random_tuple[2:-1])

# method for tuple
print(dir(my_tuple))

# get the length of the tuple
print(len(my_tuple))

# find index
print(my_tuple.index('second_value'))

# iterate
for item in my_random_tuple:
    print(item)

