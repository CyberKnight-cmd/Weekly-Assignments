# Assignment17
# Prog 2
# Write your question here(in shortened form)
# 1 + 2 + 2 + 3 + 3 + 3 + 4 + 4 + 4 + 4 +…..….. 

# Write your code here
N = int(input("Enter N = "))
series = sum([i**2 for i in range(1,N+1)])
print(series)