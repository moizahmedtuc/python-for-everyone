numberTaken = [3, 6, 10, 15, 20]

# How 'continue' work here?
# So basically when the condition is true, continue will skip all lines after it and go back start of the loop
for n in range(1, 21):
    if n in numberTaken:
        continue
    else:
        print(n)
