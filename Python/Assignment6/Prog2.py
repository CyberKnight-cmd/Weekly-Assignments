import math
a,b,c = map(float, input("Enter the sides : ").split(','))

value = (b**2 + c**2 - a**2) /(2*b*c)

print(math.degrees(math.acos(value)))