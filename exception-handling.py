"""
Exception handling is a programming technique used to gracefully manage and
respond to unexpected or exceptional situations that can occur during the execution of a program

When to use?
1. Expected errors
2. Input validation
3. Critical sections
4, Testing and debugging
"""

string_or_number = 'abc12'
try:
    string_to_int = int(string_or_number)
    print('Converted string to int:', string_to_int)
except ValueError:
    print('Invalid integer number')

#

try:
    result = 10 / 0
    print('result:', result)
except ZeroDivisionError as e:
    print('Error:', e)
    result = None
