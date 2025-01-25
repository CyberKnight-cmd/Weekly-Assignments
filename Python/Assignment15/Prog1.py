# 1 8 27 64 125 216 343 512 729 1000..
# Cubic series 

n = int(input("Enter n = "))
print(" ".join([str(i**3) for i in range(1,n+1)]))