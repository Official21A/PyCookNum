# Problem 10
# Working with matries and basics of linear algebra.
# By using numpy library and methods.
import numpy as np 

m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
"""

[1, -2,  3
 0,  4,  5
 7,  8, -9]

 """

 m.T
 """
 Transpose
[ 1,  0,  7
 -2,  4,  8
  3,  5, -9]

 """

 m.I 
 """
 Inverse
[0.33, -0.02,  0.09
 0.15,  0.13,  0.02
 0.12,  0.09, -0.01]

 """

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])

m * v
"""
[ 8,
 32,
  2]
 """

# For linear algebra we can use the linalg subpackage
import numpy.linalg

numpy.linalg.det(m) # -229.999999999993

numpy.linalg.eigvals(m) # {-13.11, 2.79, 6.35}

x = numpy.linalg.solve(m, v) # Solve for x in mx = v

# For more methods of linear algebra check the numpy methods in this field
# http://www.numpy.org