# 10. Super()
# ==========================================
# CONCEPT: Parent Access
# ==========================================
# Calls the parent method. Useful in __init__.

class Animal:
    def __init__(self):
        print("Animal Created")

class Dog(Animal):
    def __init__(self):
        super().__init__() # Call parent init
        print("Dog Created")

d = Dog()
