"""
In Python, a module is a file containing Python code that can be used in other Python programs.
Modules help organize code by grouping related functions, classes, and variables into separate files,
making it easier to maintain and reuse code across different projects.
"""


def my_name():
    print('My name is Moiz')


'''
Now if you want to use it from different program
you need to import file name and then access the function
e.g.:
import modules

modules.my_name()
'''

'''
You can download modules, and use already created modules also
Note: Import should be at the top of the file
'''

import random

x = random.randrange(1, 1000)
print(x)
