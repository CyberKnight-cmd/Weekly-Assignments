# Assignment27
# Prog 1
# Write a Python program to add three numbers using user defined function. 

# Write your code here

def addThreeNumbers(a,b,c):
    return (a + b + c)
a,b,c = map(int,input("Enter three numbers : ".split()))
print(addThreeNumbers(a,b,c))