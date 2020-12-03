# Problem 4
# Working with binary octal and hexadecimal integers.
# Since above bases are important we first explain them.

x = 1234

# binary
a = bin(x) # '0b10011010010'
# octal
b = oct(x) # '0o2322'
# hexadecimal
c = hex(x) # '0x4d2'

# Can also work with format to just create an ouput
d = format(x, 'b') # '10011010010'
e = format(x, 'o') # '2322'
f = format(x, 'x') # '4d2'

# Also works for negetive numbers
g = format(-4, 'b') # '-100'

# Final trick
# If you want to change an string number into any base
# just use int(x, y) with x as string and y as the base.
h = '3422674'
i = int(h, 2) # Gives binary output 