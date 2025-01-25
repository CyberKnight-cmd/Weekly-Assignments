# Assignment25
# Prog 2
# Write a Python program to join a list of strings into a single string. 

# Write your code here

s = [word.strip() for word in input("Enter words seperated by ',' : ").split(',')]
print("Words entered : ", s)
print("String = ",  " ".join(s))