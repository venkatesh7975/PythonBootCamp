# 19. Operator Overloading (+)
# ==========================================
# CONCEPT: Custom Math
# ==========================================
# Define what + does for your objects.

class Point:
    def __init__(self, x):
        self.x = x
    
    def __add__(self, other):
        return Point(self.x + other.x)

p1 = Point(10)
p2 = Point(20)
p3 = p1 + p2
print(p3.x) # 30
