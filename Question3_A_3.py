# Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
'''
[[ 3 -2 ]
 [ 1  0 ]]
'''

import numpy

x = numpy.array([[3, -2], [1, 0]])
print(x)

xEVal, xREVec = numpy.linalg.eig(x)

print("eigenvalues:\n", xEVal)
print("Right eigenvectors:\n", xREVec)