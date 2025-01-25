# Assignment25
# Prog 4
# Write a Python program to check if a string ends with a substring.

# Write your code here

s = input("Enter the sring : ")
subString = input("Enter the sub-sring : ")

print("Ends with the substring." if s.find(subString)==len(s)-len(subString) else "Does not end with the substring.")

# Or just use endswith()
print(s.endswith(subString))