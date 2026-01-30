# 17. Filter with Lambda
# ==========================================
# CONCEPT: Selection
# ==========================================
# Keep only items where function returns True.

nums = [1, -1, 2, -5]
positives = list(filter(lambda x: x > 0, nums))
print(positives) #[1, 2]
