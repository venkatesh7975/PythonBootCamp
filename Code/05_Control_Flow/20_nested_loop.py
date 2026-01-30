# 20. Nested Loops
# ==========================================
# CONCEPT: Matrix / Grid
# ==========================================
# A look inside a loop. O(N^2) complexity.

for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print() # Newline for next row
