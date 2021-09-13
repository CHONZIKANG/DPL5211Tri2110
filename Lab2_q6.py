# Student ID: 1201200750
# Student Name: Chon Zi Kang
import math

radius = float(input("Please enter the radius: "))

volume = (4/3)* math.pi * pow(radius,3)

surface_area = 4 * math.pi * pow(radius,2)

print("The radius input is {}".format(radius))
print("The volume is {:.2f}  " .format(volume))
print("The surface area is {:.2f} " .format(surface_area))
