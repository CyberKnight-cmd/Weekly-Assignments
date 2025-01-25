# Assignment27
# Prog 3
# Write a Python program to calculate a to the power b (a^b) using user defined function without using pow ()

# Write your code here
def power(a,b):
    return a**b

a,b = map(int, input("Enter the base and the power : ").split())
print(power(a,b))