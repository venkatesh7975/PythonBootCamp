# 4. Self
# ==========================================
# CONCEPT: Identity
# ==========================================
# 'self' refers to the specific object being used.
# It allows each object to have its own data.

class Dog:
    def __init__(self, name):
        self.name = name # My name is [name]

d1 = Dog("Rex")
d2 = Dog("Spot")
print(d1.name)
print(d2.name)
