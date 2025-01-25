a,b,c = map(float,input("Enter a number : ").split(','))
if (c<a>b):
    print(f"{a} is largest.")
elif (a<b>c):
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")