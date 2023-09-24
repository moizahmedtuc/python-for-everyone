# To print 'Moiz' 10 times
for x in range(10):
    print("Moiz")

# To print number from 0-10
for y in range(10):
    print(y)

# To print even number - 0-21 is range and what gap we want in every number is by 2
for z in range(0, 21, 2):
    print(z)

# While loop is a loop that loops until condition is true
age = 20

while age < 25:
    print(age)
    age += 1

'''
Calculate factorial
e.g. 5 x 4 x 3 x 2 x 1
'''


def calculate_factorial(n):
    if n < 0:
        return 'Factorial is not defined for negative numbers'
    factorial_num = 1
    for n in range(1, n + 1):
        factorial_num *= n
    return factorial_num


print('Factorial:', calculate_factorial(5))
