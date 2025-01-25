# Assignment26
# Prog 5
# Write a Python program to find the first non-repeating character in a string.

# Write your code here
def nonRepeatingCharacter(s):
    for character in s:
        count = 0
        for search in s:
            if character==search:
                count+=1
            if count>1:
                break
        if count==1:
            return character
    return None
s = input("Enter a string : ")
res = nonRepeatingCharacter(s)
print("All characters are repeating" if res == None else f"'{res}' is non-repeating  in '{s}''.")