import math
a, b, c = map(int,input("Enter the co-efficient : ").split(','))
center = (-a,-b)
print(center, "is the center of the circle.")
try :
    radius = math.sqrt(a**2 + b**2 - c)
except ValueError:
    print("The circle has an imaginary radius ", end=': ')
    print(complex(0,math.sqrt(abs(a**2+b**2-c))))
else:
    print(radius,"is the radius of the circle.")