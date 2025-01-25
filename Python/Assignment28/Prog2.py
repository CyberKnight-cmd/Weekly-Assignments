# Assignment28
# Prog 2
# 2, 4, 8, 16, 32, 64… 

# Write your code here

def series(n):
    l = [str(2**x) for x in range(1,n+1)]
    print(",". join(l))

series(int(input("Enter n = ")))