import os

folders = os.listdir("data") 

# os.chdir("/User")
# print(os.getcwd())  

for folder in folders:
    print(folder) 
    print(os.listdir(f"data/{folder}")) 