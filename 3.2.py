#great circle distance

# Import math Library
import math

x1,y1 = eval(input("enter point 1: "))
x2,y2 = eval(input("enter point 2: "))
r = 6371.01

d = r * math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1)-math.radians(y2)))

print("the distance between the two points is ", d," km" )
