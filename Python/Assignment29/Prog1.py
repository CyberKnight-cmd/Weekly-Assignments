# Assignment29
# Prog 1
"""Write a Python program to check whether any user input number is Armstrong number or not using user defined function. """

# Write your code here

def isArmstrong(originalNum:str):
    rev = 0
    for digits in originalNum:
        rev+=int(digits)**len(originalNum)
    return rev==int(originalNum)



num = input("Enter a number : ")
print(f"{num} is an Armstrong number" if isArmstrong(num) else f"{num} is not an Armstrong number")