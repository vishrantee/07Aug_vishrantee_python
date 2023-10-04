"""Write a Python program to calculate surface volume and area of a cylinder  """
#volume=π r² h
#surface area=2πrh+2πr2

import math
x=math.pi
r=float(input("Enter your Radius :"))
h=float(input("Enter your height :"))
volume=(x)*((r)**2)*(h)
surface=(2*x*r*h)+(2*x*((r)**2))
print("Your volume is : ",volume)
print("Your surface area is : ",surface)
