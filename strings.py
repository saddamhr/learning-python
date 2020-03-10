# STRINGS
mystring = 'abcdefg'

# mystring[0] = 'X' #'str' object does not support item assignment

# Indexing
print(mystring[3])
print(mystring[-1])

# Slicing
print(mystring[4:])
print(mystring[:3])
print(mystring[2:5])
print(mystring[::1])
print(mystring[::2])
print(mystring[::3])

# Basic Methods
x = mystring.upper()
x = mystring.lower()
x = mystring.capitalize()
mysentence = 'Hello World'
print(mysentence.split())
print(mysentence.split('o'))

# Print Formatting
x = 'Item One: {x}, Item Two: {y}'.format(x = 'dog', y = 'cat')
print(x);
