# 25. issubclass()
# ==========================================
# CONCEPT: Relation Check
# ==========================================
# Check if class is child of another.

class A: pass
class B(A): pass

print(issubclass(B, A)) # True
