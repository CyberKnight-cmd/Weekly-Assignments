# Assignment30
# Prog 5
"""Write a Python program to generate first N Fibonacci series using recursion function. """

# Write your code here

def fibo(series:list, n:int):
    if n>1:
        series.append(series[-1] + series[-2])
        return fibo(series, n-1)
    return series

n = int(input("Enter a number : "))
series = [0,1]
if n==0:
    print(series[0])
elif n==1:
    print(series)
else:
    print(fibo(series, n))
