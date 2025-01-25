l =  input().split()
item, index = l.append(input("Enter the item to be inserted : ")), int(input("Enter the position number to be inserted : "))

if -1<index<len(l):
    l = l[:index] + l[-1:] + l[index:-1]
    print(l)
else:
    print("Invalid index.")