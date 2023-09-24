"""
 A list comprehension is a concise way to create lists in Python.
 List comprehension are a powerful and readable alternative to traditional
 for loops when you need to generate or transform lists.
 Given a list of numbers, create a new list that contains only the even numbers using list comprehension.

 A basic list comprehension consists of square brackets containing an expression followed by a for loop.
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# an example of a list comprehension that squares each element of a given list?
def list_of_squares(numbers):
    return [x ** 2 for x in numbers]


print('Return square of the list:', list_of_squares(num))


# How can you add a filter condition to a list comprehension? (with given list)
def filter_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]


print('Return even numbers form list:', filter_even_numbers(num))


# How can you add a filter condition to a list comprehension? (without given list)
def filter_even_numbers():
    return [x for x in range(1, 21) if x % 2 == 0]


print(f'Return even number by range: {filter_even_numbers()}')

'''
Nested list comprehensions - Task: Generate all possible combinations of elements from 
list1 and list2 as tuples and returns them in a new list.
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']


def nested_list_comprehension():
    return [(x, y) for x in list1 for y in list2]


print(nested_list_comprehension())
