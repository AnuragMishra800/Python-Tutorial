
# Doc String in python. 

# Doc strings are not ignorable. 
# Its different from comments in python.
# but you have to write it right below of the function.

def square(n):
    '''Take a number as input from user. And print the square of the given number.'''
    return (n**2) 
n = int(input("Enter the number:"))
print(f"The square of {n} is",square(n)) 

# For printing doc string you have to write like this.
print(square.__doc__) 

# Pep in python (Python Enhancement Proposal). 
 
import this