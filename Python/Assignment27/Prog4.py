# Assignment27
# Prog 4
"""
Write a Python program to find out the summation of the series 
using user defined function- 

i) S=1+2+3+4+5+……Nth term 

"""

# Write your code here
def s(n):
    if n>1:
        return n+s(n-1)
    else:
        return 1
    
n = int(input("Enter n = "))
print(s(n))