# Classes And Objects In Python 

class Person():
    name = "Swaranjal"
    lastName = "Sharma"
    job = "Python Developer"
    salary = "9000"
    def info(self):
        print(f"{self.name} {self.lastName} is a {self.job} with the salary of {self.salary} per month.")

a = Person()
b = Person()

a.name = "Ansh"
a.lastName = "Saxena"
a.job = "Trainer"
a.salary = 10000

b.name = "Anurag"
b.lastName = "Mishra"
b.job = "Web Developer"
b.salary = 8000

a.info() 
b.info() 

print(f"{Person.name} {Person.lastName} is a {Person.job} with the salary of {Person.salary} per month.")