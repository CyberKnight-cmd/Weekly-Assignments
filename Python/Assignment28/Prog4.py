# Assignment28
# Prog 4
# 1, 2, 6, 24, 120, 720……. 

# Write your code here


def fact(a):
    if a<2:
        return 1
    else:
        return a*fact(a-1)
    
def series(n):
    l = [str(fact(i)) for i in range(1,n+1)]
    print(",".join(l))
    
# print(fact(int(input("Enter a number : "))))
series(int(input("Enter n = ")))