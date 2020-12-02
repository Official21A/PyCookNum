# Problem 2
# When working with float point numbers, we might actually 
# hit some tiny errors in calculations.
# For example :
a = 10.1
b = 3.4
print(a + b) # 13.5000000001

# These errors are a feature of the underlying CPU AND THE IEEE 754 arithmatic
# performed by its floating-point unit.

# to fix this we can work with Decimal module.
from decimal import Decimal
a = Decimal("10.1")
b = Decimal("3.4")
c = a + b

print(c) # 13.5
print(x == Decimal(13.5)) # True

