# 15. Static Method
# ==========================================
# CONCEPT: Utility
# ==========================================
# Belongs to class but doesn't need self.

class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 5))
