l = list(map(int, input().split()))

def swap(i, j, l):
    t = l[j]
    l[j] = l[i]
    l[i] = t
    return l

# Selection sort implementation
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] < l[j]:
            l = swap(i, j, l)

print(l)