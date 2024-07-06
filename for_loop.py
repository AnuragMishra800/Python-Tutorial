# For Loop In Python 

name = "Anurag"
for n in name:
    print(n, end=", ")  
    if(n=="r"):
        print("There is a R in your name bro.") 

# Same thing with List 

colors = ["Red", "Green", "Blue", "Yellow", "Black"]
for color in colors:
    print(color)
    for i in color:
        print(i) 

# Range concept in For Loop 
         
for k in range(6):
    print(k) 
for g in range(1, 11):
    print(g)
for l in range(0, 100, 5):
    print(l) 