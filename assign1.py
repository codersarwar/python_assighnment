#1. Write a recursive python function to print first N natural numbers
def add ( n) : 
  if n>0:
      
   add (n-1)
  print (n)

n=int(input("enter a number: "))
print(add(n))