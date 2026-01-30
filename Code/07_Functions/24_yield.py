# 24. Yield Expression
# ==========================================
# CONCEPT: Saving State
# ==========================================
# Generator expression (like list comp but lazy).

g = (x*x for x in range(3))
print(list(g)) # [0, 1, 4]
