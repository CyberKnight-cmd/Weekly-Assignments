def divisibility(a:int)-> str:
    return f"{a} is divisible by 7 and 11" if a%7==0 and a%11==0 else f"{a} is not divisible by 7 and 11"

print(divisibility(int(input("Enter a number : "))))