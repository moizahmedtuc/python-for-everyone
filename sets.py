"""
Sets: Set is an unordered collection of unique elements.
Sets are commonly used for tasks that involve storing and managing distinct values.
They are unordered collections
"""

groceries = {'milk', 'eggs', 'bread', 'eggs'}
print(groceries)  # Print only uniques elements

# add element in set
groceries.add('tape')
print(groceries)

# remove element in set
groceries.remove('bread')
print(groceries)

# Check if an element is in the set
if 'tape' in groceries:
    print('tape is in the set')

# Iterate through set
for element in groceries:
    print(groceries)

# Set comprehension with sorted list
squares = sorted({n * n for n in range(1, 10)})
print(squares)
