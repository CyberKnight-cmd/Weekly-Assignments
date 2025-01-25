# Assignment29
# Prog 4
"""Write a Python program to print the summation of this series using user defined function upto Nth term. 
    S=8+88+888+8888+………N """

# Write your code here

def sumOfSeries(N:int):
    if N>-1:
        return int("8"*(N+1)) + sumOfSeries(N-1)
    return 0

N = int(input("Enter N = "))
print(sumOfSeries(N))