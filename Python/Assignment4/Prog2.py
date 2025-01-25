num = int(input("Enter a number : "))
lastDigit = (num%10)*2
num = str((num//10)) + str(lastDigit)
print(num)
