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


print('Addition of 2 numbers:', add_numbers(4, 6))
