# Lambda Functions In Python 

# def square(x):
#     return x*x

def mix(fx, value):
    return 6 + fx(value) 

square = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

print(square(3)) 
print(cube(4)) 
print(avg(3,4,8)) 
print(mix(cube,3)) 

# lambda x, y: print(f'{x} * {y} = {x} * {y}') 