# Assignment30
# Prog 3
"""Write a Python program to calculate a to the power b (a^b) using recursion function. (You can’t use pow () and exponent operator) """

# Write your code here

def power(base:int, exp:int):
    if exp>=1:
        return base*power(base,exp-1)
    elif exp<=-1:
        return (1/base)*power(base,exp+1)
    else:
        return 1

a, b = map(int, input("Enter a and b : ").split())
print("Result : ", power(a,b))
