'''
Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop.
N: No of students (Read input from user)
Ex: L1: [150, 155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
'''
n = int(input("No of students: "))
studentInputWeight = []
for i in range(n):
    studentInputWeight.append(int(input("Enter weight for student: ")))
print(studentInputWeight)

kgConvert = []
for i in range(n):
    kgConvert.append(studentInputWeight[i]/2.205)
kgConvert = [round(elem, 2) for elem in kgConvert]
print(kgConvert)
