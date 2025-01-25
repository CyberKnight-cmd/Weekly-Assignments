# Assignment25
# Prog 3
# Write a Python program to check if a string starts with a substring. 

# Write your code here
s = input("Enter the string : ")
subString = input("Enter the sub-sring : ")

print("Starts with a substring." if s.find(subString)==0 else "Does not start with a substring.")

# Or just use startsWith()
# print(s.startswith(subString))