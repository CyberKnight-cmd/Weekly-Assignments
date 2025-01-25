import math

x1,x2 = map(float,input("Enter the x-coordinate of both the points :").split(','))
y1,y2 = map(float,input("Enter the y-coordinate of both the points :").split(','))

d  = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(d,"is the distance between two points.")