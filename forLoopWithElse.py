
# For loop with else in python 

ints = [1,2,3,4,5,6]
for i in ints:
    if i>4:
        break 
    print(i) 

for i in range(6):
    print(i)
    if i == 4:
        break 
else:
    print("Naah Nope!") 

i = 0
while i<7:
    print(i) 
    i = i + 1
    if i == 4:
        break
else:
    print("No!")  