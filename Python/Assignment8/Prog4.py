num = int(input("Enter the number : "))
sum, numCopy = 0, num
while(num!=0):
    sum+=(num%10)**3
    num//=10
if(sum==numCopy):
    print(numCopy, "is an armstrong number.")
else: 
    print(numCopy, "is not an armstrong number.")