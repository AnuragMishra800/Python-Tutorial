# Break statement in python 

for i in range(12):
    if(i==10):
        print("Loop Ended Because Of Break Statement.")
        break
    else:
        print("Miss")   
    print("5 X",i+1,"=",5*(i+1)) 

# Continue statement in python 

for i in range(12):
    if(i==10):
        print("Skip This Iteration Because Of Continue Statement.")
        continue
    print("5 X",i+1,"=",5*(i+1)) 

i = 0
while True:
    print(i)
    i += 1
    if(i%100 == 0):
        break

while True:
    n = int(input("Hi:"))
    print(n)
    if not n > 0:
        break 
    