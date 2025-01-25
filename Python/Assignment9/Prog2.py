num = int(input("Enter the number : "))
sum = 0
for i in range(1,num+1):
    if i%2==0:
        sum-=i
    else:
        sum+=i
print(sum,"is the sum of the given series.")