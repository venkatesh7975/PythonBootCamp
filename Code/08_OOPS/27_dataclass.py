# 27. Dataclasses
# ==========================================
# CONCEPT: Data Holder
# ==========================================
# Python writes __init__ and __repr__ for you!

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p) # Point(x=10, y=20)
