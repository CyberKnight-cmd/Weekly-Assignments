# Assignment18
# Prog 5
# Write your question here(in shortened form)

# 1/(1×3) + 1/(3×5) + 1/(5×7)…


# Write your code here

def fractional_series(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / (2 * i - 1) / (2 * i + 1)
    return total

n = int(input("Enter the number of terms: "))
print("Sum of the series:", fractional_series(n))