
# Sets Methods  

s1 = {1,2,3,8,9}
s2 = {4,5,6}
print(s1.union(s2)) 
s1.update(s2)
print(s1,s2) 

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
s5 = s3.intersection(s4)
print(s5) 

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
s5 = s3.intersection_update(s4)
print(s3)  

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
s5 = s3.symmetric_difference(s4)
print(s5)  

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
s5 = s3.difference(s4) 
print(s5)   

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
print(s3.isdisjoint(s4))  

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
print(s3.issuperset(s4)) 

s3 = {"Anurag","Ayush","Kunal","Karunesh","Faiz"}
s4 = {"Kunal","Karunesh","Faiz","Akash"}
print(s3.issubset(s4))  

l1 = {10,20,30,40,50,60}
l1.add(70)
print(l1) 

l1 = {10,20,30,40,50,60}
l2 = {70,80,90,100}
l1.update(l2)
print(l1) 

l1 = {"Anurag","Ashvin","Swaranjal"}
l2 = {"Ansh","Arpit","Anmol"}
l1.update(l2)  
print(l1) 

l1 = {"Anurag","Ashvin","Swaranjal"}
l1.remove("Anurag")
print(l1)

l1 = {"Anurag","Ashvin","Swaranjal"}
l1.discard("Anurg")
print(l1)  

m1 = {9,19,29,39,49,59,69,79,89,99}
p = m1.pop()
print(m1)
print(p) 

# del m1
# print(m1) 

m1.clear()
print(m1) 