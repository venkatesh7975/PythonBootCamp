# 25. Discard (Safe Remove)
# ==========================================
# CONCEPT: Safety
# ==========================================
# Like remove(), but no error if item missing.

s = {1, 2}
s.discard(99) # No error
print(s)
