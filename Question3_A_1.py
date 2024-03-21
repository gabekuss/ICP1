# Using NumPy create random vector of size 15 having only Integers in the range 1-20
'''
1. Reshape the array to 3 by 5
2. Print array shape.
3. Replace the max in each row by 0
'''
import numpy

# Create Array
x = numpy.random.randint(1, 20, (15))
print("Original array:\n", x)

# Reshape and print array
x = numpy.reshape(x, (3,5))
print("Reshaped array:\n", x)

# Replace the Max in each row with 0
x = numpy.where(numpy.isin(x, numpy.amax(x, axis = 1)), 0, x)
print("Edited array:\n", x)