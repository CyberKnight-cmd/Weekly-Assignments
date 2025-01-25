# Assignment23
# Prog 4
# Write a Python program to capitalize the first letter of each word. Input- hello world, Output- Hello World 

# Write your code here
s = input("Enter a string : ").split()
print(" ".join([word.capitalize() for word in s]))

# Or use title()
# s = input("Enter a string : ")
# print(s.title())