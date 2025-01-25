l =  list(map(float,input().split()))
product = l[0]
for i in l[1:]:
    product*=i
print(product)