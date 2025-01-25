num = int(input("Enter a number : "))%100
lastDigitSum = num//10 + num%10
print("%d + %i = %r " %(num//10, num%10, lastDigitSum))