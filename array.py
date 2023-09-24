"""
Implement the function findLargest(numbers), so it returns the largest number from
the [numbers| integer array.
Note: the array always contains at least one number.
"""


def find_largest(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
        

numbers = [5, 2, 9, 1, 8, 3]
result = find_largest(numbers)
print(result)
