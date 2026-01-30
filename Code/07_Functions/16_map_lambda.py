# 16. Map with Lambda
# ==========================================
# CONCEPT: Transformation
# ==========================================
# Apply function to every item in list.

nums = [1, 2, 3]
doubled = list(map(lambda x: x*2, nums))
print(doubled) # [2, 4, 6]
