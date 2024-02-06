'''
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
“The area of a circle with radius 10 is 314 meters square.”
'''
radius = 10
area = 3.14 * radius ** 2
txt = "The area of a circle with radius{radius: .0f} is{area: .0f} meters square."
print(txt.format(radius = radius, area = area))

