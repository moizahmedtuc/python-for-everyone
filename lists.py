# List is mutable, which means you can modify their contents after they are created.
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
print(list_x)

# delete whole list
removeAllValues = list_x[:] = []
print(removeAllValues)

# Extend the existing list with new list
list_y = [7, 8, 9, 10]
list_x.extend(list_y)
print(list_x)


# Reverse the list, related to slicing
def reverse_list(input_list):
    return input_list[::-1]


print(reverse_list([1, 2, 3, 4]))


# Find duplicates in list
def find_duplicates(input_list):
    duplicates = []
    for item in input_list:
        if input_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates


# List comprehension
# Given a list of numbers, create a new list that contains only the even numbers using list comprehension.
def even_numbers(input_list):
    return [x for x in input_list if x % 2 == 0]


# Remove duplicates from lists
# Write a function that takes a list as input and returns a new list with duplicates removed.
def remove_duplicates(input_list):
    return list(set(input_list))


# Rotate list elements
# Given a list and an integer k, rotate the list to the right by k steps.
def rotate_list(input_list, k):
    k = k % len(input_list)
    return input_list[-k:] + input_list[:-k]


# Merge two sorted list
# Merge two sorted lists into a new sorted list.
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged
