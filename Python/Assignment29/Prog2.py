# Assignment29
# Prog 2
"""Write a Python program to check whether any user input number is Krishnamurthy/Peterson/Strong number or not using user defined function."""

# Write your code here

def factorial(num:int):
    if num>1:
        return num*factorial(num=num-1)
    return 1

def petersonNumber(num:int):
    if num!=0:
        return factorial(num%10) + petersonNumber(num//10)
    return 0

def isPeterson(num:int):
    return num==petersonNumber(num)

number = int(input("Enter a number : "))
print(f"{number} is a Peterson number." if isPeterson(number) else f"{number} is not a Peterson number.")