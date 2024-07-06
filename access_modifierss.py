
# Access Modifier In Python 

class Employee:
    def __init__(self):
        self.__name = "Hari"
    
a = Employee()
# print(a.__name) # Can not be accessed directly 
print(a._Employee__name) # Can be accessed indirectly
print(a.__dir__()) 