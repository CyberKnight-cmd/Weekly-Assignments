# Assignment18
# Prog 2
# Write your question here(in shortened form)
#3 + 33 + 333 + 3333…

# Write your code here

def repeating_digit_series(n):
    total = 0
    term = 0
    for _ in range(n):
        term = term * 10 + 3
        total += term
    return total

n = int(input("Enter the number of terms: "))
print("Sum of the series:", repeating_digit_series(n))

