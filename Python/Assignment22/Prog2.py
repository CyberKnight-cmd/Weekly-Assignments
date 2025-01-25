# Assignment22
# Prog 2
"""
 1 2 3 4 5  
 1 2 3 4  
 1 2 3  
 1 2  
 1 
"""
# Write your code here

def stringGenerator(n):
    s = ""
    while n>=1:
        s+=f" {n}"
        n-=1
    return s[::-1]

n = int(input("Enter N = "))
print("\n".join([stringGenerator(n-i+1) for i in range(1,n+1)]))