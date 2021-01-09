# Set Example

# Sets are unordered collections of unique elements

# cannot index into a set, because order is not guaranteed
my_set = {1, 6, 2, 'java', 'ruby', 8, 9,10,21, 1000, 'python'}
programming_set = {'java', 'ruby', 'javascript', 'python', 'c'}

print(my_set)

# use set to remove duplicates from a list
my_list_with_dups = [1, 2, 3, 3, 4]
my_set_without_dups = set(my_list_with_dups)
print(my_set_without_dups)


# check if item is in set
print(3 in my_set_without_dups)

# math operations
print(my_set.intersection(programming_set))
print(my_set.union(programming_set))
print(my_set.difference(programming_set))


# iterate
for item in my_set:
    print(item)