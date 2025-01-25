# Assignment19
# Prog 2
# Write your question here(in shortened form)
# 3, 7, 13, 21, 31..........

# Write your code here

def progressive_series(n):
    term = 3
    for i in range(n):
        print(term, end=", " if i < n - 1 else "\n")
        term += 2 * (i + 1) + 1

n = int(input("Enter the number of terms: "))
progressive_series(n)

