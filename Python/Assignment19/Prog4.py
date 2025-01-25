# Assignment19
# Prog 4
# Write your question here(in shortened form)
# 0, 5, 14, 27, 44…

# Write your code here


def quadratic_series(n):
    for i in range(n):
        term = i**2 + 5 * i
        print(term, end=", " if i < n - 1 else "\n")

n = int(input("Enter the number of terms: "))
quadratic_series(n)
