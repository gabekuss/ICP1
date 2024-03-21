# Write a NumPy program to create a new shape to an array without changing its data.
'''
Reshape 3x2:
[[ 1 2 ]
 [ 3 4 ]
 [ 5 6 ]]
Reshape 2x3:
[[ 1 2 3 ]
 [ 4 5 6 ]]
'''

import numpy

x = numpy.array([[1, 2], [3, 4], [5, 6]])
print("Reshape 3x2:\n", x)
x = numpy.reshape(x, (2,3))
print("Reshape 2x3:\n", x)