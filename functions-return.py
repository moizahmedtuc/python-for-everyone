"""
With 'function' we can write a certain piece of code inside it and use it
whenever wherever we want to
In python you can create a function by 'def'
"""


def show_me_my_age(age):
    print('My age is:', age)


show_me_my_age(27)

'''
'Return' is used to return the values. 'Return' exit the function and send the value of 'result' back to caller
'''


def add_numbers(a, b):
    result = a + b
    return result


added_value = add_numbers(4, 6)
print('Addition of 2 numbers:', added_value)


# Write a function with return statement, with age and next to it the allowed age to date
def persons_age_limit(age):
    girls_age = age / 2 + 7
    return girls_age


for item in range(15, 60):
    print(item, persons_age_limit(item))


# OR
def persons_age_limit():
    age_limits = []
    for item in range(15, 60):
        girls_age = item / 2 + 7
        age_limits.append((item, girls_age))
    return age_limits


age_limits_list = persons_age_limit()
for age, limit in age_limits_list:
    print(f"Person's age: {age}, Dating age limit: {limit}")
