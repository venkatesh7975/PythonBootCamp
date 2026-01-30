# 14. Getters and Setters
# ==========================================
# CONCEPT: Controlled Access
# ==========================================
# Use @property to make methods look like variables.

class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("Age can't be negative")
        else:
            self._age = value

p = Person(10)
p.age = -5 # Validation runs!
