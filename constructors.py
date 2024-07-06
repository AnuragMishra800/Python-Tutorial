
# Constructors In Python 

class Person:
    def __init__(self, n, j):
        print("Hey this side person.")
        self.name = n 
        self.job = j

    def info(self):
        print(f"{self.name} is a {self.job}") 

a = Person("Anurag", "Developer")
b = Person("Kunal", "Mern-Stack Developer") 
a.info()
b.info() 