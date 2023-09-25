"""
A dictionary is a built-in data type used to store collections of key-value pairs.
Dictionaries are sometimes referred to as associative arrays or hash maps in other programming languages.
"""

class_mates = {'Moiz': 'Good in learning', 'Tom': 'Like to travel', 'Kim': 'Study hard'}
print(class_mates)

# To get the value of a specific key

print(class_mates['Moiz'])

# OR

print(class_mates.get('Moiz'))

# loop through the dictionary. Set key to 'k' and value to 'v' and class_mates.items() is for each item to loop through

for k, v in class_mates.items():
    print(k, '', v)

# Modify value
class_mates['Kim'] = 'Tim'
print(class_mates)

# Add new key value
class_mates['new_name'] = 'Not sure'
print(class_mates)

# Delete entry
class_mates.pop('new_name')
print(class_mates)

# OR by

del class_mates['Kim']
print(class_mates)

# Check for existence
if 'Moiz' in class_mates:
    print("Key 'Moiz' exists in the dictionary")

# Dictionary comprehension
squares = {x: x * x for x in range(1, 6)}
print(squares)

# Find min, max and sort dictionary
dict_stocks = {'VW': 200, 'Mercedes': 100, 'Audi': 500}
print(min(zip(dict_stocks.values(), dict_stocks.keys())))
print(max(zip(dict_stocks.values(), dict_stocks.keys())))
print(sorted(zip(dict_stocks.values(), dict_stocks.keys())))
