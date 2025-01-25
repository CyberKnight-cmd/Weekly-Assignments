# Assignment34
# Prog 1
"""Write a Python program to rotate a list in left"""

# Write your code here

matrix = [list(map(int, input(f"Row {i+1} : ").split())) for i in range(3)]

# Rotating it into left
"""
1 2 3       3 6 9
4 5 6  -->  2 5 8
7 8 9       1 4 7
"""

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=' ')
    print()