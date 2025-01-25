# Assignment18
# Prog 1
# Write your question here(in shortened form)
# 1 + (1+4) + (1+4+4^2) + (1+4+4^2+4^3)…


# Write your code here
def nested_summation_series(n):
    total = 0
    current_sum = 0
    for i in range(n):
        current_sum += 4 ** i
        total += current_sum
    return total

n = int(input("Enter the number of terms: "))
print("Sum of the series:", nested_summation_series(n))

