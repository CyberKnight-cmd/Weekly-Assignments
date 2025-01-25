# Assignment17
# Prog 3
# Write your question here(in shortened form)
# 1^2^3 + 2^3^4 + 3^4^5 + ....


# Write your code here

series = sum([(i**(i+1))**(i+2) for i in range(1,int(input("Enter N = "))+1)])
print(series)