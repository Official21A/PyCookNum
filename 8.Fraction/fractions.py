# Problem 8 
# You are in a situation where you need to work with fractions.
# We use the 'fractions' module to do the operations
from fractions import Fraction 

# Initialize
a = Fraction(5, 4) # 5/4
b = Fraction(7, 16) # 7/16

# Operations
c = a + b # 27/16
d = a * b # 35 / 64

# Getting numerator/denominator
print(d.numerator) # 35
print(d.denominator) # 64

# Converting to float
e = float(d) # 0.546875

# Limiting the denominator
f = d.limit_denominator(8) # 4/7

# Converting float to fraction
x = 3.75
y = Fraction(*x.as_integer_ratio()) # 15/4

# Although it might work correctly at most of the times ,
# but this library might give wrong answers in some complicated calculations ,
# since its needed to be under surviliance while working with.