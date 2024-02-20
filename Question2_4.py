# Write a function that takes a list and returns a new list with unique items of the first list.
# Sample List: [1,2,3,3,3,3,4,5]
# Unique List: [1, 2, 3, 4, 5]

def uniqueList(x):
    uniqueList = []

    for i in x:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList

list1 = [1,2,3,3,3,3,4,5]
print("Sample List: ", list1)
print("Unique List: ", uniqueList(list1))
