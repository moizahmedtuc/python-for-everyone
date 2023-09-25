# Write file
file_write = open('test.txt', 'w')
file_write.write('I am learning Python')
file_write.close()

# Read file
file_read = open('test.txt', 'r')
text = file_read.read()
print(text)
