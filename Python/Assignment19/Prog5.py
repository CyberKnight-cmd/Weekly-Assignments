# Assignment19
# Prog 5
# Write your question here(in shortened form)
# 3, 6, 18, 24, 45, 54...

# Write your code here

def mixed_multiples_series(n):
    for i in range(1, n + 1):
        if i % 2 == 1:  # Odd index
            term = i * 3
        else:  # Even index
            term = i * (i + 1)
        print(term, end=", " if i < n else "\n")

n = int(input("Enter the number of terms: "))
mixed_multiples_series(n)
