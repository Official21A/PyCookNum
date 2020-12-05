# Problem 6
# Working with complex numbers, and performing mathmatical operations on them.
# They can be used very simple in two ways
a = complex(2, 4) # 2 + 4j
b = 3 - 5j

# Methods
a.real # 2
a.imag # 4
a.conjugate() # 2 - 4j

# Math
c = a + b # 5 - j
d = a * b # 26 + 2j
e = a / b # 23.. + 63.. j

# To do complicate operations use cmath library
import cmath
f = cmath.sin(a)
g = cmath.exp(b)
h = cmath.cos(c)

# Ex
import math
i = math.sqrt(-1) # Runtime error ...
i = cmath.sqrt(-1) # j
