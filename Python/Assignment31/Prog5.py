l = list(map(int,input().split()))

item = int(input())
for index, i in enumerate(l):
    if i==item:
        print(index, "is the position of", item)
        break