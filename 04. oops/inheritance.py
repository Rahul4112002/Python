'''Inheritance Example'''

#Single Inheritance
class FactoryMumbai: #Parent class
    def hello(self):
        print('Hello from Factory Mumbai')
        
class FactoryPune(FactoryMumbai): #child class
    pass

obj = FactoryPune()
obj.hello()


#Multi level Inheritance
class Factory:
    def __init__(self, material, zips):
        self.material = material
        self.zips = zips
        
class BhopalFactory(Factory):
    def __init__(self, material, zips, color):
        super().__init__(material,zips)
        self.color = color

class PuneFactory(Factory):
    def __init__(self,material, zips, color, pockets):
        super().__init__(material, zips)
        self.color = color
        
#Multiple Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"Animal name: {self.name}")
        
class Human:
    def __init__(self, age):
        self.age = age

    def show(self):
        print(f"Human age: {self.age}")
        
class Robot(Human, Animal):
    pass

obj = Robot()