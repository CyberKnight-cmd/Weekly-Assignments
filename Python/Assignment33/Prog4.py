l = list(map(float, input().split()))
even, odd = [], []
for i in l:
    if i%2:
        odd.append(i)
    else:
        even.append(i)


print(even)
print(odd)