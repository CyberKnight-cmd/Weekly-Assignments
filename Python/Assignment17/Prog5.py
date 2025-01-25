# Assignment17
# Prog 5
# Write your question here(in shortened form)
#  1/1! + 1/2! + 1/3! +...+ 1/N!


# Write your code here
def fact(n):
    if n<2:
        return 1
    else:
        return n*fact(n-1)
    
series = [i/fact(i) for i in range(1,int(input("Enter N = ")) + 1)]
print(sum(series))