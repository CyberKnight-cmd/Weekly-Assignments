# Catalan Number Series

def factorial(n):
    return 1 if n<2 else n*factorial(n-1)

def catalan(n):
    return factorial(2*n)/(factorial(n+1)*factorial(n))

n = int(input("Enter n = "))
print(" ".join([str(int(catalan(i))) for i in range(n)]))