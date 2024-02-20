# Write a code that appends the type of elements from a given list.
# Input
#       x = [23, ‘Python’, 23.98]
# Expected output
#       [23, 'Python', 23.98]
#       [<class 'int'>, <class 'str'>, <class 'float'>]

x = [23, "Python", 23.98]
classList = []

for i in range(len(x)):
    classList.append(type(x[i]))

print(x)
print(classList)
