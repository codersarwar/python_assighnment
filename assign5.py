#5. Write a recursive python function to calculate sum of cubes of first N natural numbers

def nodd(n):
    if n==1:
        return 1
    else:
       
        return n*n*n+nodd(n-1)
        
nod=int(input("enter a number: "))
print(nodd(nod))