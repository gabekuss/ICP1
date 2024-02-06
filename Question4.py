it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#• Find the length of the set it_companies
print("it_companies Length: ", len(it_companies))

#• Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

#• Insert multiple IT companies at once to the set it_companies
updateSet = {"Grimbot", "Skibble"}
it_companies = set.union(it_companies, updateSet)
print(it_companies)

#• Remove one of the companies from the set it_companies
it_companies.remove("Twitter")
print(it_companies)

#• What is the difference between remove and discard
print("remove() will raise an error if the item doesn't exist while discard() will just continue regardless")

#• Join A and B
print ("Union: ", A.union(B))

#• Find A intersection B
print ("Intersection: ", A.intersection(B))

#• Is A subset of B
print("Subset: ", A.issubset(B))

#• Are A and B disjoint sets
print("Disjoint: ", A.isdisjoint(B))

#• Join A with B and B with A
print("A with B: ", A.union(B))
print("B with A: ", B.union(A))

#• What is the symmetric difference between A and B
print("Symmetric_difference; ", A.symmetric_difference(B))

#• Delete the sets completely
A.clear()
print("A: ", A)
B.clear()
print("B: ", B)

#• Convert the ages to a set and compare the length of the list and the set
ageSet = set(age)
print("age: ", len(age))
print("ageSet: ", len(ageSet))
