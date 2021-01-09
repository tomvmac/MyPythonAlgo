# Dict, Set, Tuple Example

# Dict
# Keys are immutable

my_dictionary = {'name': 'mashrur', 'course': 'python'}

phone_dict = {'mashrur': '555-55-5555',
              'zoolander': '999-99-0000',
              'jon_snow': 'fail-o-so-bad'}

word_dict = {
            'a':
                 {
                    'apple': 'the round fruit of a tree of the rose family',
                    'ant' : 'an insect which cleans up the floor'
                 },
            'b':
                {
                    'bad': 'of poor quality or low standard',
                    'business': 'season 8 of GOT'
                }
            }

# print dict
print(my_dictionary)

# get value from dict
print(word_dict['a'])
# get nested value
print(word_dict['b']['business'])


# using method
print(my_dictionary.get('name'))

# set values using methods
my_dictionary['job'] = 'python programmer'
print(my_dictionary.get('job'))

# get all keys of the dict
print(my_dictionary.keys())

# get all values of dict
print(my_dictionary.values())

# items - list all key and values of dict
print(my_dictionary.items())

# iterate through all key value pairs
for k, v in my_dictionary.items():
    print(k, v)