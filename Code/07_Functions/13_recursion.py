# 13. Recursion
# ==========================================
# CONCEPT: Self-Calling
# ==========================================
# A function calling itself. Must have a Stop Condition (Base Case).

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
