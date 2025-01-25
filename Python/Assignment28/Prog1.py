# Assignment28
# Prog 1
# 1, 4, 9, 16, 25, 36…… 

# Write your code here


def series(n):
    l = [str(x**2) for x in range(1,n+1)]
    print(",". join(l))

series(int(input("Enter n = ")))