#3. Write a recursive python function to print first N odd natural numbers

def nodd(n):
    if n==1:
        return 1
    else:
        print((2*n)-1)
        nodd(n-1)
nod=int(input("enter a number: "))
nodd(nod)