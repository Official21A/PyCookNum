# Problem 7
# You need to create or test for the floating point values of infinity, negetive
# infinity, or NaN ( not a number )
a = float('inf') # a is now infinity
b = float('-inf')

c = float('nan')

# The best way to compare and check them is to use math methods
d = math.isinf(a) # True
e = math.isnan(c) # True

# This would not work correctly
f = a is b
g = float('nan') # Gives false
h = g == c # Gives false

# You can also use them in calculations
i = a + 45 # infinity
j = math.sqrt(c) # nan

# Nan and infinity values propagate all operations without raising an exception.