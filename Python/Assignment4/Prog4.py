num = input("Enter the decimal : ")
if(num.__contains__('.')):
    position = num.find('.')
    num = num[0:position] + "1" + num[position:len(num)]
    print(num)
else:
    print("Not a decimal number.")