# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Ages: ", ages)

# • Sort the list and find the min and max age
ages.sort()
print("Sorted Ages: ", ages)

# • Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
ages.sort()
print ("Values Added: ", ages)

# • Find the median age (one middle item or two middle items divided by two)
middle = (len(ages) - 1) // 2
print ("Median: ", ages[middle])

# • Find the average age (sum of all items divided by their number)
sum = 0
for i in range(len(ages)):
    sum += ages[i]
print ("Average age: ", sum / len(ages))
# • Find the range of the ages (max minus min)
print ("Age range: ", max(ages) - min(ages))
