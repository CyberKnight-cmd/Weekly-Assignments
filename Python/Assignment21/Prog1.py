n = int(input("Enter N = "))
print("\n".join([" "*i + "*"*(n+1-i) for i in range(1,n+1)]))
# 