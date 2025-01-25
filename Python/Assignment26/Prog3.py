# Assignment26
# Prog 3
# Write a Python program to find the length of the longest word in a string. 

# Write your code here
s = input("Enter a string : ").split()
max = 0
for word in s:
    max = len(word) if max<len(word) else max
print(max)