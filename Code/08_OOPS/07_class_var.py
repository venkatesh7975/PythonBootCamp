# 7. Class Variables
# ==========================================
# CONCEPT: Shared Data
# ==========================================
# Shared by ALL objects of that class.

class Dog:
    kind = "Canine" # Class Variable

d1 = Dog()
d2 = Dog()
print(d1.kind) # Canine
print(d2.kind) # Canine
