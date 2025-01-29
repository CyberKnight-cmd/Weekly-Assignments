# 10001000100101

a = input()

for i in range(len(a)):
    if a[i]=="1":
        for j in range(i+1, len(a)):
            if a[j]=="1":
                temp = len(a[i:j]) - 1
                i = j
                break 
        print(temp)