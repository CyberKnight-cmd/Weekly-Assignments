a,b,c = map(int,input("Enter the co-efficients : ").split(','))
if(b==0):
    print("The line is vertical")
else:
    slope = round(-a/b,3)
    print("The slope of the given line is", slope)