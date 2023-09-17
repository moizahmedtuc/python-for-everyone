firstName = "Abdul "
print(firstName + '\nMoiz')

# Print something repeatedly
# It will print Abdul 5 times
print(firstName * 5)

# Whenever you have '' in your sentence replace it with ""
sentence = "I don't know what to do"
print(sentence)

# Whenever you have \n in your sentence you need to place 'r' at the start of the sentence,
# otherwise \n just moves the rest sentence to a new line
sentence = r'c:\user\dell\name'
print(sentence)

# Print specific word from string
print(sentence[0])
print(sentence[-1])
# Slicing in python
print(sentence[3:7])
print((sentence[:7]))

# To count characters count in a string, we use length function
sentenceLength = len(sentence)
print(sentenceLength)