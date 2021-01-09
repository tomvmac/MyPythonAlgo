# List Examples 1

# Things to cover for lists:
# 1. Sort - sort(), sorted()
# 2. Find - len(), min(), in, indexing, slicing, count()
# 3. Insert/Remove - append(), insert(), extend(), remove(), pop()
# 4. Sub-lists - slicing, in-place, copying
# 5. Iteration - for loops, while loops


my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10, 15]
# indices  0   1  2  3   4   5   6  7   8  9
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]
my_new_list = ["art", "econ"]

#Sort
# print(f"Ints: {my_list}")
# print(f"Strings: {my_strings_list}")
# print("Sorting")
# sortedList = sorted(my_list)
# print(f"Sorted Ints via function: {sortedList}")
# print("Id of sortedList ", id(sortedList))
#
# my_list.sort()
# print(f"Sorted Ints again via method: {my_list}")
# print("Id of my_List ", id(my_list))

# Find
print("physics" in my_strings_list)
print(15 in my_list)

# find a value
print(my_strings_list.index("philosophy"))

# len of string
# get length of last element
print(my_list[len(my_list)-1])
print(my_list[-1])

# min function
print(min(my_list))

# show all methods
print(dir(my_list))

# append, insert, extend
# append
my_list.append(25)
print(my_list)

# insert
my_list.insert(4, 99)
print(my_list)

# extend - extends the list with elements from another list
my_list.extend(my_new_list)
print(my_list)

# remove values from list
my_strings_list.remove("comp sci")
print(my_strings_list)

# pop - removes the last object of list and returns what you pop or removed
my_strings_list.pop()
print(my_strings_list)

# sublists

print("Sublists...")

# slicing
print(my_list[0:4])

# slicing with step size
# get every other element from beginning to end
print(my_list[0:-1:2])

# Iteration

# for loop
print("for loop - print items on list")
for item in my_list:
    print(item)
