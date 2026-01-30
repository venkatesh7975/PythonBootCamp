# 23. Generator
# ==========================================
# CONCEPT: Lazy Evaluation
# ==========================================
# Uses yield instead of return. Returns an iterator.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter)) # 1
print(next(counter)) # 2
