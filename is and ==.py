a = 4
b = 4
print(a is b) # Exact Location Of Object In Memory
print(a==b) # Value

a = 4
b = "4"
print(a is b)
print(a==b)

a = (2,3)
b = (2,3)
print(a is b)
print(a==b)

a = "Anurag"
b = "Anurag"
print(a is b)
print(a==b)

a = [2,4,6]
b = [2,4,6]
print(a is b)
print(a==b)

a = None 
b = None
print(a is None) 
print(a is b)
print(a==b)