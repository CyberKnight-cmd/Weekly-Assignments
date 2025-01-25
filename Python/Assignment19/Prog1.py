# Assignment19
# Prog 1
# Write your question here(in shortened form)
# 0, 3/1, 8/3, 15/5..... 
# Write your code here

def fractional_series(n):
    for i in range(1, n + 1):
        numerator = i**2 - 1
        denominator = 2 * i - 1
        print(f"{numerator}/{denominator}", end=", " if i < n else "\n")

n = int(input("Enter the number of terms: "))
fractional_series(n)
