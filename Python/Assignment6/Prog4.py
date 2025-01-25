import math
a, b, c = map(int,input("Enter the values : ").split(','))
D = b**2 - (4*a*c)
if(D>0):
    print("Roots are distinct and real")
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("Roots of the given quadratic equation is : %i,%r" %(x1,x2))
else:
    print("Roots are imaginary")
    print(complex(a, b),end=', ')
    print(complex(a,-b), end='')
    print(" are the roots of the given quadratic equation")