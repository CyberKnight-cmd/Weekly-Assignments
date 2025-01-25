# Finding the GCD 
x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))
while y:
        x, y = y, x % y
print("The GCD of the two numbers are :", x)