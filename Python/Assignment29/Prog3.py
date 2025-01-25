# Assignment29
# Prog 3
"""Write a Python program to check whether any user input number is palindrome number or not using user defined function. """

# Write your code here

def isPalindrome(num:str):
    return num==num[::-1]

number = input("Enter a number : ")
print(f"{number} is palindrome." if isPalindrome(number) else f"{number} is not palindrome.")