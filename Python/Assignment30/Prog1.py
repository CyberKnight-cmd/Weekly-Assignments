# Assignment30
# Prog 1
""" Write a Python program to calculate the summation of N natural numbers using recursion function. """

# Write your code here

def sum(num : int):
    if num>0:
        return num + sum(num-1)
    else:
        return 0

n = int(input("Enter n = "))
print(sum(n))