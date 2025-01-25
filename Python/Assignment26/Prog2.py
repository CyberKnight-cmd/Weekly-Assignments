# Assignment26
# Prog 2
# Write a Python program to reverse each word in a string.

# Write your code here

s = [word[::-1] for word in input("Enter a string : ").split()]
print("\n".join(s))