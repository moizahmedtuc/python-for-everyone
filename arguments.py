"""
When we don't know exactly how many arguments we will be passing, so use * with any argument name
We can also say it's 'Flexible number of arguments'
"""


def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    return total


print(add_numbers(3))
print(add_numbers(3, 4, 5))

'''
Unpacking arguments
'''


def health_checkup(age, apples_ate, smok_cig):
    result = (100 - age) + (apples_ate * 3) - (smok_cig * 2)
    print(result)


Moiz_data = [27, 30, 10]
health_checkup(Moiz_data[0], Moiz_data[1], Moiz_data[2])

# But it makes code length and lengthy, instead do unpacking of arguments by just putting *
# It takes the list and passes each itme in the list, one at a time
health_checkup(*Moiz_data)
