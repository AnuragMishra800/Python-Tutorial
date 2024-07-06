# Decorators In Python 

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using it.")
    return mfx

@greet
def hello():
    print("Hello World")

# @greet 
def add(a, b):
    print(a+b)

hello()
greet(add)(2,6) 