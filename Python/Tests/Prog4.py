def swap(listOfTuples, i, j):
    t = listOfTuples[i]
    listOfTuples[i] = listOfTuples[j]
    listOfTuples[j] = t
    return listOfTuples

n = int(input("Enter n = "))
listOfTuples = list(tuple(input(f"Enter the elements of tuple {i+1}: ").split()) for i in range(n))

for i in range(n):
    for j in range(i+1, n):
        if listOfTuples[i][1]>listOfTuples[j][1]:
            listOfTuples = swap(listOfTuples, i, j)

print(listOfTuples)