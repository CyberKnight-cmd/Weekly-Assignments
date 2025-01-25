# Assignment17
# Prog 1
# Write your question here(in shortened form)
# -1 + 2 + 11 + 26 + 47 +…

# Write your code here
N = int(input("Enter N = "))
series = [-1]
for i in range(N-1):
    series.append(series[i]+3*(2*i + 1))
print(series," = ",sum(series))