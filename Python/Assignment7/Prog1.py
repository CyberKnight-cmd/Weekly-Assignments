num = int(input("Enter a number :"))
digit = 0
while num>0:
    digit = digit*10 + (num%10)
    num//=10
print(digit)