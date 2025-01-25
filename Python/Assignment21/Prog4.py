n = int(input("Enter N = "))
print("\n".join([" "*i + "*"*(2*(n-i-1)+1) for i in range(n)]))