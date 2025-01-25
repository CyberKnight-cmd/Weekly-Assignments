# Assignment18
# Prog 4
# Write your question here(in shortened form)
# 1^2 + (1^2+2^2) + (1^2+2^2+3^2)


# Write your code here

def summation_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += sum(j ** 2 for j in range(1, i + 1))
    return total

n = int(input("Enter the number of terms: "))
print("Sum of the series:", summation_of_squares(n))