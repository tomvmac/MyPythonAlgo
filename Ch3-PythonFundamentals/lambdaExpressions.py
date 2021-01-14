# lambda expression are on the fly functions

def my_math_func(x, f):
    return f(x)

# explicit function to return x cubed
def x_cube(x):
    return x**3

# lambda expression to return x cubed
my_cube_lambda = lambda x:x**3

print(my_math_func(2, my_cube_lambda))


my_letters = ['a', 'b', 'c']

# cap all letters using map
print(list(map(str.capitalize, my_letters)))

# cap letters with lambda expression
print(list(map(lambda x:x+x.capitalize(), my_letters)))

# generate random int
from random import randint
my_ints = [randint(1,1000) for num in range(1000)]
print(my_ints)
# use lambda against list
print(list(map(lambda x:x*2, my_ints)))
