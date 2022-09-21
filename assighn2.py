#2. Write a recursive python function to print first N natural numbers in reverse order
def revrs(n):
    if n>0:
        print(n)
        revrs(n-1)
s=revrs(10)
print(s)
