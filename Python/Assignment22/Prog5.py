# Assignment22
# Prog 5
# Write your question here(in shortened form)
"""
        1  
      2 2  
    3 3 3  
  4 4 4 4  
5 5 5 5 5   
  4 4 4 4  
    3 3 3  
      2 2  
        1
"""
# Write your code here
n = int(input("Enter n = "))
print("\n".join(["  "*(n-i) + f"{i} "*i for i in range(1,n+1)]))
print("\n".join(["  "*(n-i) + f"{i} "*i for i in range(n-1,0,-1)]))