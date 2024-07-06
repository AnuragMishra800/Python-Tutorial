# Operations In Tuple 

country = ("India","Russia","Singapore","Italy","England")
connect = list(country)
connect.append("Spain")
connect.pop(2)
connect[2] = "Germany"
country = tuple(connect)
print(country) 

tuple1 = (1,2,3,4,5)
tuple2 = (6,6,6,6,7,8,9,10) 
tuple3 = tuple1+tuple2
print(tuple3)
print("Count of 6 is",tuple2.count(6)) 
print("Index of 6 in tuple3 is",tuple3.index(6)) 
print("The total length of tuple3 is",len(tuple3))  

my_tuple = (1, 2, (3, 4), 5)
print(my_tuple[2][1])

# my_tuple = (1, 2, 3)
# my_tuple[1] = 4