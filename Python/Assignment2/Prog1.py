import math
a,b,c = map(float,input("Enter a side of the triangle : ").split(','))
s = (a + b + c )/2
print(math.sqrt(abs(s*(s-a)*(s-b)*(s-c))))
