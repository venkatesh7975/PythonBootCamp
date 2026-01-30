# 11. Polymorphism
# ==========================================
# CONCEPT: Many Forms
# ==========================================
# Different classes having same method name.

class Cat:
    def speak(self): print("Meow")

class Dog:
    def speak(self): print("Woof")

animals = [Cat(), Dog()]
for a in animals:
    a.speak() # Knows which one to call!
