# Write a function that accepts a string and calculate the number of upper-case letters and lower-case
# letters.
# Input String: 'The quick Brow Fox'
# Expected Output:
#       No. of Upper-case characters: 3
#       No. of Lower-case Characters: 12

def letterCase(x):
    upper = sum(1 for i in x if i.isupper())
    lower = sum(1 for i in x if i.islower())
    print("No. of Upper-case characters: ", upper)
    print("No. of Lower-case characters: ", lower)

inputString = "The quick Brow Fox"
print("Input String: ", inputString)
letterCase(inputString)

