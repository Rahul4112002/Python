'''Polymorphism - Method Overriding'''

class Animal:
    def show(self):
        print("Hello I am Animal")
        
class Human(Animal):
    def show(self):
        print("Hello, I am Human")
        
obj1 = Animal()
obj2 = Human()
obj1.show()
obj2.show()