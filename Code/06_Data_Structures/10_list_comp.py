# 10. List Comprehension
# ==========================================
# CONCEPT: Pythonic Loops
# ==========================================
# Create a list in one line. [expr for item in iterable]

# Old way
squares = []
for x in range(5):
    squares.append(x**2)

# New way
sq = [x**2 for x in range(5)]
print(sq)
