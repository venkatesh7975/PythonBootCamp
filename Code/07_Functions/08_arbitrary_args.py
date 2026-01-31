# 8. Arbitrary Args (*args)
# ==========================================
# CONCEPT: Unlimited Input
# ==========================================
# Collects extra arguments into a Tuple.

def sum_all(*numbers):
    
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_all(1, 2, 3, 4)) # 10