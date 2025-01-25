# Assignment26
# Prog 4
# Write a Python program to find the length of the smallest word in a string. 

# Write your code here

s = input("Enter a string : ").split()
min = len(s[0])
for word in s:
    min = len(word) if min>len(word) else min
print(min)