a,b,c = map(float,input("Enter a number : ").split(','))
if (c>a<b):
    print(f"{a} is smallest.")
elif (a>b<c):
    print(f"{b} is smallest.")
else:
    print(f"{c} is smallest.")