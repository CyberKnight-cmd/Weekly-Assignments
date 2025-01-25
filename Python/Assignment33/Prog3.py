l = list(map(float, input().split()))
max_val = l[0]
second_largest = -float('inf')  # Set to negative infinity initially

for i in l:
    if i > max_val:
        second_largest = max_val  # Current max becomes second largest
        max_val = i  # New max found
    elif second_largest < i < max_val:  # Check if it's the second largest
        second_largest = i

print(second_largest)
