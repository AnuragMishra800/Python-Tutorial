
# Uses and differences of local and global variables in python 
x = 4
print(x)

def hello():
    x = 5
    print(f"Local x is {x}")
    print("Done, Anurag") 

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")

z = 8

def hi():
    global y
    y = 7
    print(z)

hi()
print(y) 