str = input("Enter a string : ")
i = 0
try: 
    for i in range(1000):
        print(str[i],"=",i)
        i+=1
except IndexError:
    print("Total characters in the string is", i)
