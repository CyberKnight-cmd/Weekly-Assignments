# Assignment28
# Prog 3
# 1, 3, 7, 13, 21, 31..

# Write your code here

def series(n):
    l = [str(sum([2*j for j in range(i)]) + 1) for i in range(n+1)][1:]

    print(",". join(l))

series(int(input("Enter n = ")))