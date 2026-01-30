# 22. MRO (Method Resolution Order)
# ==========================================
# CONCEPT: Search Order
# ==========================================
# Where does python look for methods first?

class A: pass
class B(A): pass
class C(B): pass

print(C.mro()) # C -> B -> A -> Object
