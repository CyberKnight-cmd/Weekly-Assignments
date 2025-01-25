# Assignment30
# Prog 2
"""Write a Python program to calculate the factorial of any user given input number using recursion function. """

# Write your code here

def factorial(num:int):
    if num>1:
        return num*factorial(num-1)
    return 1

number = int(input("Enter a number : "))
print(factorial(number))