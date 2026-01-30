# 5. Swapping Variables
# ==========================================
# CONCEPT: Pythonic Magic
# ==========================================
# In other languages, you need a Temp variable to swap 2 items.
# In Python, do it in one line!

a = 5
b = 10

print(f"Before: a={a}, b={b}")

# The Magic Swap
a, b = b, a

print(f"After: a={a}, b={b}")
