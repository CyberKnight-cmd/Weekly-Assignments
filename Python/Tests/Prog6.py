def getInput()-> dict:
    items = int(input("How many items do you want to input in the dictionary ? \n"))
    
    dictionary  = {}

    for i in range(items):
        key = int(input("Enter Key : "))
        value = input("Enter Value : ")
        dictionary[key] = value

    return dictionary
def getCopiedKeys(dictionary1, dictionary2):
    copiedKeys = [key for key in dictionary1 if key in dictionary2]
    return copiedKeys

print("Enter the values for dictionary 1 : ")
dict1 = getInput()
print("Enter the values for dictionary 2 : ")
dict2 = getInput()
print(getCopiedKeys(dictionary1=dict1, dictionary2=dict2))