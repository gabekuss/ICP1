# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements),
# also print the shape, type and data type of the array

import numpy

x = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], numpy.int32)
print(x)
print("shape:", x.shape)
print("dtype:", x.dtype)