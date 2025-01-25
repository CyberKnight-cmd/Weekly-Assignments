l =  input().split()
index = int(input("Enter the position number whose item is to be deleted : "))

if -1<index<len(l):
    l = l[:index] + l[index+1:]
    print(l)
else:
    print("Invalid index.")