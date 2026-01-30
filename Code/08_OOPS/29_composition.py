# 29. Composition
# ==========================================
# CONCEPT: Has-A Relation
# ==========================================
# An object CONTAINING other objects (Use variables instead of inheritance).

class Engine:
    def start(self): print("Vroom")

class Car:
    def __init__(self):
        self.engine = Engine() # Car HAS AN Engine
    
    def drive(self):
        self.engine.start()

c = Car()
c.drive()
