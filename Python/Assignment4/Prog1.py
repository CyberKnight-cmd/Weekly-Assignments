num = input("Enter a number :")
num = num[0:-3] + num[-1] + num[-2] + num[-3]
print(num)