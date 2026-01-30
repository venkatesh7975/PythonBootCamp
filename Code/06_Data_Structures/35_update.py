# 35. Update
# ==========================================
# CONCEPT: Merge
# ==========================================
# Adds keys from another dict. Overwrites if present.

d1 = {"a": 1}
d2 = {"b": 2, "a": 100}
d1.update(d2)
print(d1) # {'a': 100, 'b': 2}
