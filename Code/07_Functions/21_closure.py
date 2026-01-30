# 21. Closure
# ==========================================
# CONCEPT: Function Factory
# ==========================================
# Inner function remembers outer variables even after outer finishes.

def multiplier(n):
    # Returns a function that multiplies by n
    return lambda x: x * n

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10)) # 30
print(times5(10)) # 50
