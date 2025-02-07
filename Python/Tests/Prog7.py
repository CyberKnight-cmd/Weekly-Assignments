def exampleProg1(n : str):
    choice, count = int(input("Enter your choice : ")), 0
    match(choice):
        case 1:
            for character in n:
                if character>='A' and character<='Z' :
                    count += 1
        case 2:
            for character in n:
                if character>='a' and character<='z':
                    count+=1
        case 3:
            for character in n:
                if isVowel(character):
                    count+=1
        
    print(count)

def exampleProg2(n : str):
    n = n.split()
    string, count = input("Enter a word : "), 0
    for word in n:
        if (string.lower()==word.lower()):
            count += 1
    print(f"The frequency of thew word \"{string}/{string.lower()}\" is : {count}")

def exampleProg3(n:str):
    print("".join(sorted(list(n.casefold()))))
    # n = n.casefold
    

def isVowel(a : str):
    a = a.lower()
    return a=='a' or a=='e' or a=='i' or a=='o' or a=='u'


if __name__ == "__main__":
    n = input("Enter a string : ")
    exampleProg3(n)
    