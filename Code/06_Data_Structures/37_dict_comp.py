# 37. Dictionary Comprehension
# ==========================================
# CONCEPT: One-Liner Dict
# ==========================================
# {k:v for item in iterable}

nums = [1, 2, 3]
sq_dict = {x: x**2 for x in nums}
print(sq_dict) # {1: 1, 2: 4, 3: 9}
