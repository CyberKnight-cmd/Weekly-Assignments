a, b, c, p,q,r = map(int, input("Enter the values : ").split(','))

determinant = a*q - p*b

if(determinant==0):
    print("The lines are parallel and co-efficients")
else:
    x = c*q - r*b
    y = a*r - p*c
    print("(%d,%i) is the point of intersection of the given lines"%(x,y))