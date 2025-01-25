# Assignment19
# Prog 3
# Write your question here(in shortened form)

# 3, 20, 63, 144, 230…

# Write your code here

def cubic_growth_series(n):
    for i in range(1, n + 1):
        term = i**3 + 2
        print(term, end=", " if i < n else "\n")

n = int(input("Enter the number of terms: "))
cubic_growth_series(n)
