# A list in Python is a built-in data structure used to store a collection of items.
# List is mutable, which means you can modify their contents after they are created.

# How do you create an empty list in Python?
# Answer: You can create an empty list by using [] or by calling the list() constructor
my_list1 = []
# Create an empty list named my_list2. You can append it later
my_list2 = list()

list_x = [1, 2, 3, 4, 4]
print(list_x)
# Print value from specific position
print(list_x[0])

# To change value in the list
list_x[4] = 5
print(list_x)

# 1. To add value to the list, this adds items permanently
list_x.append(6)
print(list_x)
# 2. To add value to the list, list_x is not updated. The updated list is in addNewValues variable
addNewValues = list_x + [7, 8]
print(addNewValues)

# Slicing in list
print(list_x[1:4])
# Replace multiple items/values at once
list_x[0:1] = [0, 1]
print(list_x)

# Remove/delete some values/items in the list
list_x[0:2] = []
print('Remove values form 0 to 1 index in list x:', list_x)

# OR
# The remove() method is used to remove the first occurrence of a specific value from a list.
list_x.remove(6)
print('Remove value from the list by item', list_x)

# The pop() method is used to remove an element at a specific index and returns the removed value
removed_value = list_x.pop(2)
print('Remove an elements by its value from the list:', list_x)
print('Removed value:', removed_value)

# The del statement can be used to remove an element by its index
del list_x[2]
print('Removes an element by its index:', list_x)

# Delete whole list
list_x[:] = []
print('Remove all values from list:', list_x)

# Extend the existing list with new list
list_y = [7, 8, 9, 10]
list_x.extend(list_y)
print(list_x)


# Reverse the list, related to slicing
def reverse_list(input_list):
    return input_list[::-1]


print('1. Reverse list:', reverse_list([1, 2, 3, 4]))
# OR

list_x.reverse()
print('2. Reverse list:', list_x)
# Adds the elements from tuple
tuple_x = (99, 100)
list_x.extend(tuple_x)
print('Extend list from tuple', list_x)
# Get the minimum value from the list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
minimum_value = min(my_list)
print("Minimum value:", minimum_value)

# Check if an element is in a list - use the in keyword to check if an element is present in a list
item = 8
if item in list_x:
    print(item, 'is in the list')
else:
    print(f'Can not find the {item} in the list')


# Remove duplicates in the given list and sort them
# Write a function that takes a list as input and returns a new list with duplicates removed and also sort the lsit
def remove_duplicates(input_list):
    uniques_values = []
    for items in input_list:
        if items not in uniques_values:
            uniques_values.append(items)
    return uniques_values


num = [100, 99, 3, 4, 99, 4]
num.sort()
print("Showing uniques values/remove duplicated values in the list", remove_duplicates(num))


# Find duplicates in list
def find_duplicates(input_list):
    duplicates = []
    for items in input_list:
        if input_list.count(items) > 1 and items not in duplicates:
            duplicates.append(items)
    return duplicates


num = [100, 99, 3, 4, 99, 4]
num.sort()
print("1. Showing duplicated values in the list", find_duplicates(num))


# Find duplicate values in the list
def find_duplicate_values(input_list):
    unique_values = []
    duplicates = []
    for items in input_list:
        if items not in unique_values:
            unique_values.append(items)
        else:
            duplicates.append(items)
    return duplicates


num = [100, 99, 3, 4, 99, 4]
num.sort()
print(f"2. Showing duplicated values in the list {find_duplicate_values(num)}")


# Rotate list elements
# Given a list and an integer k, rotate the list to the right by k steps.
def rotate_list(input_list, k):
    k = k % len(input_list)
    return input_list[-k:] + input_list[:-k]


num = [1, 2, 3, 4, 5]
print(rotate_list(num, 2))


# Merge two sorted lists into a new sorted list.
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0

    # Compare and merge until one list is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # Append any remaining elements of list1 (if any)
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # Append any remaining elements of list2 (if any)
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print('Merged list:', merged_list)
