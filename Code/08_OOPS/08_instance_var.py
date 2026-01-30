# 8. Instance Variables
# ==========================================
# CONCEPT: Unique Data
# ==========================================
# Unique to EACH object. Defined in __init__ using self.

class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("A")
d2 = Dog("B")
# d1.name is A, d2.name is B
