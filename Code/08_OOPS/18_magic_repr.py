# 18. Magic Method (__repr__)
# ==========================================
# CONCEPT: Developer String
# ==========================================
# Output for developers/debugging.

class Dog:
    def __repr__(self):
        return "Dog()"

d = Dog()
print(repr(d))
