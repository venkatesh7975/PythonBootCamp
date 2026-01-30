# 17. Magic Method (__str__)
# ==========================================
# CONCEPT: String Representation
# ==========================================
# Controls what print(obj) shows.

class Dog:
    def __str__(self):
        return "I am a Dog"

d = Dog()
print(d)
