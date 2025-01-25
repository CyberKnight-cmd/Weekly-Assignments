# Assignment22
# Prog 4
"""
5 4 3 2 1  
4 3 2 1  
3 2 1  
2 1  
1  
2 1  
3 2 1  
4 3 2 1  
5 4 3 2 1  
"""
# Write your code here

def stringGenerator(a,turn):
    s = ""
    match turn:
        case 0:
            while(a>=1):
                s+=f"{a} "
                a-=1
            return s
        case 1:
                while(a>=2):
                    s+=f"{a} "
                    a-=1
                return s
        case _:
            return None
n = int(input("Enter n = "))
print("\n".join([stringGenerator(i,turn=0) for i in range(1,n+1)][::-1]))
print("\n".join([stringGenerator(i,turn=0) for i in range(2,n+1)]))