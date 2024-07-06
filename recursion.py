# Recursion in python 

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter the number:"))
print(f"The factorial of {n} is",fact(n))  

# Fabonacci Sequence in python 

n = int(input("Enter the number:"))
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
for i in range(n):
    print(fibonacci(i))  