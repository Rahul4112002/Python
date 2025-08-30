"""Dunder Methods Example"""

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal: {self.name}, Age: {self.age}"

    def __add__(self, other):
        return self.age + other.age


lion = Animal("Lion", 12)
tiger = Animal("Tiger", 15)

print(lion)          # __str__
print("Total age =", lion + tiger)  # __add__
