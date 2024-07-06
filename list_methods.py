#  Some Important List Methods 

lst = [1,21,32,32,5,126,6,57,68,44,5,65,565] 
print(lst)
lst.append(99)
print(lst)
lst.sort()
print(lst)
lst.reverse()
print(lst)
print(lst.index(5)) 
mst = lst.copy()
print(mst)  
mst.insert(0,99999)
print(mst)
lst.extend(mst)
print(lst) 
# kst = lst + mst 
# print(kst) 