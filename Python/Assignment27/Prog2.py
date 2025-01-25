# Assignment27
# Prog 2
#Write a Python program to calculate the factorial using user defined function. 

# Write your code here
def fact(a):
    if a<2:
        return 1
    else:
        return a*fact(a-1)
    
print(fact(int(input("Enter a number : "))))