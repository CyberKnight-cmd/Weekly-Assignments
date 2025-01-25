# Assignment22
# Prog 1

""" 1 
    22 
    333 
    4444 
    55555 
"""
# Write your code here

n = int(input("Enter N = "))
print("\n".join([f"{i}"*i for i in range(1,n+1)]))