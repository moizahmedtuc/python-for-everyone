# Tuple is immutable, Tuples are similar to lists, but once you create a tuple, you cannot change its elements
tuples = (1, 2, 3, 4, 5)
print(tuples)


# TypeError: 'tuple' object does not support item assignment
# tuples[4] = 6
# print(tuples)


# Swap Two Values with a Tuple:
# Problem: Write a function that takes two values and swaps them using a tuple.
def swap_values(a, b):
    return b, a


print(swap_values(1, 2))


# Find the Largest and Smallest Values in a Tuple:
# Problem: Write a function that takes a tuple of numbers and returns the largest and smallest values as a tuple.

def find_extremes(numbers):
    return min(numbers), max(numbers)


random_numbers = (1, 2, 3, 4, 5, 6)
print(find_extremes(random_numbers))


# Tuple Concatenation:
# Problem: Write a function that concatenates two tuples and returns a new tuple.

def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2


tuple_abc = (1, 2, 3)
tuple_xyz = (4, 5, 6)
print(concatenate_tuples(tuple_abc, tuple_xyz))
