principal = float(input("Enter the prinicpal amount : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time in yrs : "))
n = int(input("Enter the no. of times interest compounded : "))

compoundInterest = principal*((1+(rate/n))**(n*time)) - principal

print("The simple interest is %d"%compoundInterest)

