# File Operations In Python 
# Open Operation 

f = open('myfile.txt', 'w')
text = f.write() 
print(text)
f.close() 

# Write Operation 

f = open('myfile.txt', 'r')
text = f.read()
print(text)
f.close() 

# Append Operation

f = open('myfile.txt', 'a')  
f.write(" Hello World!") 

# Use With In File Opeartions

with open('myfile.txt', 'a') as f:
    f.write(" Owner Of Review State.") 