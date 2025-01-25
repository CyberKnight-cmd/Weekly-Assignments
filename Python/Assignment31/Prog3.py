l = list(map(int,input().split()))

min = l[0]
# 24 12 42 5 36 89 90 108 100
for i in l:
    min = i if i<min else min


print(min)