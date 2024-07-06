
# Dictionary In Python 

marks = {
    507 : "Anurag Mishra",
    510 : "Ayush Shriwastav",
    520 : "Kunal",
    530 : "Shanu",
    550 : "Ansh",
    600 : "Arpit"
}
print(marks[507]) 
print(marks[510]) 
print(marks[520]) 
print(marks[530]) 
print(marks[550]) 
print(marks[600]) 
print(marks) 

drive = {
    "name" : "Anurag Mishra",
    "age" : 17,
    "eligible" : False
}
print(drive['name']) 
print(drive.get('eligible')) 
print(drive.keys())  
print(drive.values())
print(drive.items()) 

for key in drive.keys():
    print(f"The value of drive corresponding to the key {key} is {drive[key]}.")  

for key ,value in drive.items():
    print(f"The value of drive corresponding to the key {key} is {value}.") 