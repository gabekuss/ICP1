# Compute the sum of the diagonal element of a given array.
'''
[[ 0 1 2 ]
 [ 3 4 5 ]]
'''

import numpy

x = numpy.array([[0, 1, 2],[3, 4, 5]])
print("Initial Array:\n", x)

print("Sum of the diagonal element of the array:", (sum(numpy.diagonal(x))))