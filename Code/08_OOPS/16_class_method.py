# 16. Class Method
# ==========================================
# CONCEPT: Factory
# ==========================================
# Takes 'cls' instead of 'self'. Can create objects.

class Person:
    kind = "Human"
    
    @classmethod
    def get_kind(cls):
        return cls.kind

print(Person.get_kind())
