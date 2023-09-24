# 'for' loops are typically used for looping through elements of an iterable directly.

foods = ['chicken', 'beef', 'lamb']

for f in foods:
    print(f)
    print(len(f))

for f in foods[0:2]:
    print(f)

'''    
'While' loop used when the condition for continuation is based on some logic or state, 
and the exact number of iterations is not known ahead of time.
When waiting for a particular state or condition to be met.
Repeating an action until a certain criterion is satisfied.
'''
count = 0
while count < 5:
    print(count)
    count += 1
