# Assignment27
# Prog 5
"""
Write a Python program to find out the summation of the series 
using user defined function- 

ii) S=1+3+5+7+9+……Nth term  

"""

# Write your code here

def s(n):
    if n>0:
        return (2*n+1)+s(n-1)
    else:
        return 1
    
n = int(input("Enter n = "))-1
print(s(n))