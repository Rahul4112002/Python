'''Classes and Objects'''
#simple class
class Factory:
    a = 12 #class attribute
    
    def hello(self): #class method
        print("Hello from Factory class")
        
obj1 = Factory()
obj1.hello()


#Class with constructor
class FactoryWithInit:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets
        
    def show(self):
        print(f"Material: {self.material}, Zips: {self.zips}, Pockets: {self.pockets}")

reebok = FactoryWithInit('Leather', 3,2)
reebok.show()

