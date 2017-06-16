# python program for the circle area and circumference
import math

pi=math.pi

#storing the input of the radius value
a=input('Enter the Radius : ')
r= int(a)
# formula for the area and circumference
area= pi*r*r

circumference= 2*pi*r

print(area)
print(circumference)