num = input("Enter a number :")
rev =""
for i in range(len(num)):
    rev += num[len(num)-1-i]
    i += 1
if int(num)==int(rev):
    print(num, "is palindrome.")
else:
    print(num,"is not palindrome.")