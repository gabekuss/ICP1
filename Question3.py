# • Create a tuple containing names of your sisters and your brothers (imaginary siblings are
#   fine)
brothers = ("Test1", "Test2")
sisters = ("Test3", "Test4")
print("Brothers: ", brothers, "\nSisters: ", sisters)

# • Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print("Siblings Tuple: ", siblings)     # The formatting when this prints confuses me a bit

# • How many siblings do you have?
print("Number of Siblings: ", len(siblings))

# • Modify the siblings tuple and add the name of your father and mother and assign it to
#   family_member
family_member = siblings + ("father", "mother")
print("Family Members: ", family_member)
