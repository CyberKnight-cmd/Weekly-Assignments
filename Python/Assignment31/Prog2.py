l = list(map(int,input().split()))

max = l[0]
# 24 12 42 5 36 89 90 108 100
for i in l:
    max = i if i>max else max


print(max)