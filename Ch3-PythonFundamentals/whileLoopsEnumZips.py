# While loops

from random import randint

truth_condition = True

l1 = [randint(1, 100) for num in range (1000)]

i = 0
num_to_search = 25
while i < len(l1):
    if l1[i] == num_to_search:
        print(f"{num_to_search} found at index {i}")
        break
    i+=1

# enumerate
for index, num in enumerate(l1):
    if l1[index] == num_to_search:
        print(f"{num_to_search} found at index {index}")
        break


# while loops should be used when you don't know when to end


# combining two lists into tuple using zip
l1 = ['.py', '.js', '.rb', '.java', '.c']
l2 = ['python', 'javascript', 'ruby', 'java', 'c']
tuple_list = list(zip(l2, l1))
print(tuple_list)

