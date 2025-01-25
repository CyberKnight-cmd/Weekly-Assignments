# Assignment23
# Prog 3
# Write a Python program to capitalize the first letter of your input string. Input- hello world, Output- Hello world 


# Write your code here
s = input("Enter a string : ").strip()
print(s[0].upper() + s[1:])

# Or use capitalize()
# print(s.capitalize())