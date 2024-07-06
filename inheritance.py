
# Inheritance In Python 

class Employee:
    def __init__(self, name, id):
        self.name = name 
        self.id = id 
    def show(self):
        print(f"Name of employee is {self.name} and his id is {self.id}.") 

class Programmer(Employee):
    def showLang(self):
        print("Default language is Python.") 

e1 = Employee("Anurag", 99)
e1.show() 
e2 = Programmer("Ansh", 98)
e2.show() 
e2.showLang() 