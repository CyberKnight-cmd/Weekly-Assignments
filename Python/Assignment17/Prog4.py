# Assignment17
# Prog 4
# Write your question here(in shortened form)
# 1/1^1 + 1/2^2 + 1/3^3

# Write your code here
series = [1/(i**i) for i in range(1,int(input("Enter N = "))+1)]

print(sum(series))