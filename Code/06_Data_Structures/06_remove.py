# 6. Remove
# ==========================================
# CONCEPT: Deletion by Value
# ==========================================
# Removes the FIRST matching value.

L = [1, 2, 3, 2]
L.remove(2) # Removes the first 2
print(L) # [1, 3, 2]

# Common Error: L.remove(99) (ValueError if not found)
