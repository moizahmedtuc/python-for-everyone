magicNumber = 20

# This program will loop till 50 even it finds the magic number, so why waste computer memory
for n in range(51):
    if n is magicNumber:
        print(n, 'is a magic number')
    else:
        print(n)

# So add 'break' in your loop, when it finds the magic number it breaks and terminated the loop
for n in range(51):
    if n is magicNumber:
        print(n, 'is a magic number')
        break
    else:
        print(n)

# Print numbers from range 0-100 which are multiple of 4
for x in range(101):
    if x % 4 == 0:
        print(x, 'is a multiple of 4')