def factorial(a):
    if(a<=1):
        return 1
    return a*factorial(a-1)
num = int(input("Enter the number : "))
sum = 0
numCopy = num
while(num!=0):
    sum+=factorial(num%10)
    num//=10
if(numCopy==sum):
    print(numCopy, " is a Peterson's number.")
else:
    print(numCopy, " is not a Peterson's number.")