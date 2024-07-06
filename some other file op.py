# Some  Other Important File Operations In Python 

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break  


# An example to use it 

# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0]) 
#     m2 = int(line.split(",")[1]) 
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student{i} in Math is: {m1}")  
#     print(f"Marks of student{i} in English is: {m2}")  
#     print(f"Marks of student{i} in Science is: {m3}")  

#     print(line) 

# Seek, Tell And Truncate Method 

# with open('myfile.txt','r') as f:
#     print(type(f)) 

#     f.seek(10)

#     print(f.tell())
#     data = f.read(9) 
#     print(data) 

# with open('sample.txt', 'w') as f:
#       f.write("Just A Everyday Regular Normal.") 
#       f.truncate(20) 

# with open('sample.txt', 'r') as f:
#       print(f.read()) 