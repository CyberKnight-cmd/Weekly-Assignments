num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
lastDigit1 = num1%10
lastDigit2 = num2%10
product = ((num1//10)*10+lastDigit2)*((num2//10)*10+lastDigit1)
print(product)