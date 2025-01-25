# Assignment22
# Prog 3
"""
55555  
4444 
333 
22  
1
"""
# Write your code here

n = int(input("Enter N = "))
print("\n".join([f"{n-i+1}"*(n-i+1) for i in range(1,n+1)]))