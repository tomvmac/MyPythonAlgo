# List Examples 1

# Things to cover for lists:
# 1. Sort - sort(), sorted()
# 2. Find - len(), min(), in, indexing, slicing, count()
# 3. Insert/Remove - append(), insert(), extend(), remove(), pop()
# 4. Sub-lists - slicing, in-place, copying
# 5. Iteration - for loops, while loops


my_list = [15, 6, 7, 8, 35, 12, 14, 4, 10]
my_strings_list = ["comp sci", "physics", "elec engr", "philosophy"]

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