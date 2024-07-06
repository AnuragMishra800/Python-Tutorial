# List in python 
store = [1,23,4.5,"Anurag","Mishra",True,False]
print(store)
print(type(store))
print(store[0]) 
print(store[1]) 
print(store[2]) 
print(store[3]) 
print(store[4]) 
print(store[5]) 
print(store[6])  
print(store[-3])  
print(store[len(store)-3])    
print(len(store)) 
print(store[:])
print(store[2:5])
print(store[1:6:2])
if "Anurag" in store:
    print("Yes")
else:
    print("No") 
if 4.5 in store:
    print("Yes")
else:
    print("No") 
if 456 in store:
    print("Yes")
else:
    print("No") 
if "Mis" in "Anurag Mishra":
    print("Hmm")
else:
    print("Nah") 
# List Comprehension 
lst = [i for i in range(6)] 
print(lst) 
lst = [i for i in range(20) if i%2==0] 
print(lst) 