# 2. Memory Visualization
# ==========================================
# CONCEPT: RAM & Addresses
# ==========================================
# Variables are just fancy names for memory addresses (like house addresses).
# 'id()' shows the memory address.

a = 10
b = 20
c = 10 # Points to SAME address as 'a' for efficiency!

print(f"Address of a (10): {id(a)}")
print(f"Address of b (20): {id(b)}")
print(f"Address of c (10): {id(c)}")
