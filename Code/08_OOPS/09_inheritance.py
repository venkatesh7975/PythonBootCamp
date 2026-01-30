# 9. Inheritance
# ==========================================
# CONCEPT: Hierarchy
# ==========================================
# Child class gets everything from Parent class.

class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print("Woof")

d = Dog()
d.eat() # Inherited!
d.bark()
