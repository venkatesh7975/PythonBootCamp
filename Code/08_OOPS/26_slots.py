# 26. __slots__
# ==========================================
# CONCEPT: Optimization
# ==========================================
# Prevents creating dynamic attributes to save memory.

class Point:
    __slots__ = ['x', 'y']

p = Point()
p.x = 10
# p.z = 5 # Error! Not in slots.
