# Generators, yield

# list comprehension
l1 = [num for num in range(1,11)]

# list generator
l1 = (num for num in range(1,11))
print(l1)
print(next(l1))
print(next(l1))


my_cubed_ints = map(lambda x: x**3, l1)
# print(list(my_cubed_ints))
# print(next(my_cubed_ints))



# writing your own mash_map generator function
# def mash_map(f, some_iterable):
#     for item in some_iterable:
#         yield f(item)

# list comprehension
# def mash_map(f, some_iterable):
#     return [f(item) for item in some_iterable]

# return a generator
# def mash_map(f, some_iterable):
#     return (f(item) for item in some_iterable)


# print(l1)
# my_cubed_ints = mash_map(lambda x: x**3, l1)
# print(my_cubed_ints)
# print(next(my_cubed_ints))
# print(next(my_cubed_ints))
# print(list(my_cubed_ints))
