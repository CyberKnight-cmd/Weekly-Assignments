import math

a, b, c, d, e = map(float, input("Enter the values : ").split(','))

distance = (a*c + b*d + e)/math.sqrt(c**2 + d**2)

print(distance, "is the distance between the point and the line.")
