# Use looping to output the elements from a provided list present at odd indexes.

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(len(my_list)):
    if (i % 2 == 1):
        print ("index", i, ": ", my_list[i])
