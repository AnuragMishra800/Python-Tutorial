
# If else Statement In Short 
a = 10
b = 20
print("A") if a > b else print("=") if a == b else print("B") 

c = 9 if a < b else 0
print(c) 

n = input("Enter your name: ") 
d = int(input("Enter your age: "))
print(f"Congratulations {n}, you can drive.") if  d >= 18 else print(f"Ohh sorry {n}, you can not drive.")  

n = input("Enter your name: ")
m = int(input("Enter your marks: ")) 
print(f"Congratulations {n}, you pass the exam.") if  m >= 33 else print(f"Ohh sorry {n}, you fail in the exam.")  
