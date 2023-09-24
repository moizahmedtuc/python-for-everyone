import re

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
# use 'f' before the start of the string, so it know there is a expression in the string
# String interpolation
print(f'path = {sentence}')

# Print specific word from string
print(sentence[0])
print(sentence[-1])
# Slicing
print(sentence[3:7])
print(sentence[:7])

# To count characters count in a string, we use length function
sentenceLength = len(sentence)
print('Count string length:', sentenceLength)

# Convert a string to integer
string = '123'
string_to_int = int(string)
print('String to integer:', string_to_int)

# Reverse string
print('Reverse string:', sentence[::-1])


# OR
def reverse_string(sentence):
    return ' '.join(reversed(sentence.split()))


print(reverse_string(sentence))


# String Transformation (Capitalize the first letter)
def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())


s = "hello wORLD"
result = capitalize_words(s)
print('Capitalize the first letter of each word in string:', result)

# convert string to upper case
print(s.upper())
# lower case
print(s.lower())


# Regular Expressions (Extract all email addresses from the string)
def extract_emails(s):
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', s)


print(extract_emails(
    "Contact us at info@example.com and support@example.org"))  # Output: ['info@example.com', 'support@example.org']

'''
Palindrome Check: Determine if a string is a palindrome 
(a word, phrase, number, or other sequences of characters which reads the same backward or forward).
'''


def is_palindrome(s):
    return s == s[::-1]


s = 'Madam'
print(is_palindrome(s))


# Substring count - Write a function to count the occurrences of a substring in a given string.
def count_substring(main_string, substring):
    return main_string.count(substring)


main_string = 'Moiz! How are you Moiz?'

print('Moiz occurs', count_substring(main_string, 'Moiz'), 'times in the main string')

'''
Replace character in string
'''


def replace_character_in_string(string, index, char):
    if not (isinstance(string, str) and isinstance(index, int) and isinstance(char, str)):
        return 'Wrong input'
    if index < 0 or index > len(string):
        return 'Index out of bound'

    return string[:index - 1] + char + string[index:]


print('Replace character in string:', (replace_character_in_string('Test', 2, 'a')))

'''
create a function that takes a string and returns a new string where 
every vowel is replaced by the next vowel in the sequence ('a' -> 'e', 'e' 
-> 'i', 'i' -> 'o', 'o' -> 'u', 'u' -> 'a').
'''


def replace_vowels(s):
    vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a'}

    new_string = ""
    for char in s:
        if char in vowel_map:
            new_string += vowel_map[char]
        else:
            new_string += char

    return new_string


# Test the function
test_string = "hello"
print(replace_vowels(test_string))
