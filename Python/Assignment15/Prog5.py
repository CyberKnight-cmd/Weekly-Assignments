def lucas(term):
    if term==0:
        return 2
    elif term==1:
        return 1
    else:
        return lucas(term-1) + lucas(term-2)
    
print(" ".join([str(lucas(i)) for i in range(int(input("Enter the term : ")))]))