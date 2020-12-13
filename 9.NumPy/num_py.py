# Problem 9
# When working with large numbers or vectors, mathmatical operations can take
# alot of time and space, and you might not get a correct answer.
# By using python library "numpy" we can save alot of time and space.
# Python lists 
x = [1,2,3,4]
y = [5,6,7,8]

x * 2 # [1,2,3,4,1,2,3,4] not what we wanted
x + 10 # Gives traceback
x + y # [1,2,3,4,5,6,7,8] not exactly what we wanted but no tracebacks :)

# Using numpy
import numpy as np 
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])

ax * 2 # [2,4,6,8]
ax + 10 # [11,12,13,14]
ax + ay # [6,8,10,12]
ax * ay # [5,12,21,32]

# We can even create a function and do mathmatical operations on array , and
# python treats it like a single number
def f(x):
	return 3*x**2 - 2*x + 7

az = f(ax) # an array of size 4

# We can create two demention arrays and work with them just like vectors
grid = np.zeros(shape=(10000,10000), dtype=float)
"""
Result:

[0.0 , 0.0 , 0.0 , .......... , 0.0
 0.0 , 0.0 , 0.0 , .......... , 0.0
 0.0 , 0.0 , 0.0 , .......... , 0.0
 ..................................
 ..................................
 0.0 , 0.0 , 0.0 , .......... , 0.0]

"""

grid += 10 # each element will be added to 10
np.sqrt(grid) # it squers every element in the grid

# There is more you can do with 2D arrays
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

a[1] # [5,6,7,8]

a[:,1] # [2,6,10]

a[1:3,1:3] # [[6,7],[10,11]]

a + [100,101,102,103] # Adds the vector to every row

np.where(a < 10, a, 10) # A conditional statement that converts numbers larger
						# than 10 to 10 in array a
