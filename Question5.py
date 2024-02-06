#The radius of a circle is 30 meters.
radius = 30

#• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
_area_of_circle_ = (radius * radius) * 3.14
print("Area: ", _area_of_circle_)

#• Calculate the circumference of a circle and assign the value to a variable name of
#_circum_of_circle_
_circum_of_circle_ = 2 * 3.14 * radius
print("Circumference: ", _circum_of_circle_)

#• Take radius as user input and calculate the area
userRadius = int(input("Enter a Radius\n"))
userArea = (userRadius * userRadius) * 3.14
print("Area of your circle is: ", userArea)
