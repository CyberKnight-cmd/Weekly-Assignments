def returnPattern(s):
    return (s + s[-2:]*4)

print(returnPattern(input("Enter a string : ")))