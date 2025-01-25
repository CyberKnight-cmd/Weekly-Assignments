num = int(input("Enter the number : "))
newNum = (num//100)*100+(num%10)*10 + ((num%100)//10)
print(newNum, "is the number obtained after exchanging last two digits.")