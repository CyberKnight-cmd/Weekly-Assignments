num = int(input("Enter a positive integer : "))
value = 1
while(num!=0):
    value*=num
    num -= 1
print(value, "is the factorial")