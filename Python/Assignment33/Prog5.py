l = list(map(float, input().split()))

s = l[0]
for index, i in enumerate(l[1:]):
    s += i
    l[index+1] = s

print(l)