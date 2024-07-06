
class Math:
    def __init__(self, num):
        self.num =  num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b 
    
result = Math.add(10,20)
print(result) 
a = Math(5)
print(a.num) 
a.addtonum(6)
print(a.num)
print(Math.add(3,5))

class MyClass:
    @staticmethod
    def static_method():
        print("Hello from static method")

    def instance_method(self):
        print("Hello from instance method")
        self.static_method()

obj = MyClass()
obj.instance_method()
