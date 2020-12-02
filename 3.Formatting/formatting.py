# Problem 3
# To format a number for output, specially when working with floats.
x = 1234.56789

# Two decimal places of accuracy
a = format(x, '0.2f') # 1234.57

# Right justified in 10 chars, one digit accuracy
b = format(x, '>10.1f') # '    1234.6'

# Left justified
c = format(x, '<10.1f') # '1234.6    '

# Centered
d = format(x, '^10.1f') # '  1234.6  '


# Adding seperator for thousands
e = format(x, ',') # 1,234.56789

f = format(x, '0,.1f') # 1,234.6


# If you want to use exponential notation , change f to an e or E
g = format(x, 'e') # 1.2345678e+03

h = format(x, '0.2E') # 1.23E+03