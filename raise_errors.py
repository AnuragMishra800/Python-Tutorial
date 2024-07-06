# Raising Custom Errors In Python 

a = int(input("Enter Any Value Between 5 To 10: "))

if(a<5 or a>10):
    raise ValueError("Value should be between 5 to 10.") 

a = input("Enter your name: ")

if(a=="Quit"): 
    raise SyntaxError("No Quit accepted.") 

b = int(input("Enter any value except 99 or 999: "))

if(b==99 or b==999):
    raise ValueError("Bola tha ki 99 aur 999 nhi.") 

# We Can Throw Many Errors By Using Raise Keyword.

try:
    raise KeyError("Key not found")
except KeyError as e:
    print(e)

try:
    raise IndexError("Index out of range")
except IndexError:
    print("Caught an index error")
finally:
    print("Executing finally block")
