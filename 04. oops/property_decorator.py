"""Property Decorator Example"""

class Animal:
    @property
    def show(self):
        return "Hello, I am using @property"


obj = Animal()
print(obj.show)   # access like an attribute, not method
