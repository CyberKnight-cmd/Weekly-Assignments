# Assignment18
# Prog 3
# Write your question here(in shortened form)
# (3^3 – 2^3) + (5^3 – 4^3) + (7^3 – 6^3)…

# Write your code here

def difference_of_cubes(n):
    total = 0
    for i in range(1, n + 1):
        term = (2 * i + 1) ** 3 - (2 * i) ** 3
        total += term
    return total

n = int(input("Enter the number of terms: "))
print("Sum of the series:", difference_of_cubes(n))

