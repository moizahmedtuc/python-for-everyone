# List is mutable
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

list_y = [7, 8, 9, 10]
list_x.extend(list_y)
print(list_x)
