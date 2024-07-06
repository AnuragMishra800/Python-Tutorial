# MAP
 
def cube(x):
    return x*x*x

l = [1,2,3,4,5]

# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(cube,l))
# newl = tuple(map(cube,l)) 
print(newl) 

# FILTER 

def filter_function(a):
    return a>2
    # r = [ls * 2 for ls in l if ls > 2]
    # return r 

newl2 = list(filter(filter_function,l)) 
# newl2 = filter_function(l) 
print(newl2)

# REDUCE 

from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]
sum = reduce(lambda a,b: a+b, numbers) 
print(sum) 