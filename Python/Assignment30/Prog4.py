# Assignment30
# Prog 4
"""Write a Python program to check whether any use given input number is Armstrong number or not using recursion function. """

# Write your code here
def generatingNumber(num, length):
    if(num!=0):
        return (num%10)**length + generatingNumber(num//10, length)
    return 0

def isArmstrong(originalNum:str):
    return int(originalNum)==generatingNumber(int(originalNum), len(originalNum))


num = input("Enter a number : ")
print(f"{num} is an Armstrong number" if isArmstrong(num) else f"{num} is not an Armstrong number")