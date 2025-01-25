def stringGenerator(n):
    s = ""
    while n>=1:
        s+=f"{n}"
        n-=1
    return s[::-1]

n = int(input("Enter N = "))
print("\n".join([stringGenerator(i) for i in range(1,n+1)]))